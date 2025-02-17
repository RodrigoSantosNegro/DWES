import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser, Evento, Comentario, Reserva
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


def sesion(request):
    contexto = {
        'nombre': 'Django',
        'version': 4.0,
    }
    return render(request, 'inicio.html', contexto)

def inicio(request):
    contexto = {
        'nombre': 'Django',
        'version': 4.0,
    }
    return render(request, 'inicio.html', contexto)

def detalle_evento(request):
    contexto = {
        'nombre': 'Django',
        'version': 4.0,
    }
    return render(request, 'inicio.html', contexto)

def reservas_usuario(request):
    contexto = {
        'nombre': 'Django',
        'version': 4.0,
    }
    return render(request, 'inicio.html', contexto)


# Create your views here.

# CRUD de eventos:
def listar_eventos(request):
    if request.method == 'GET':
        titulo = request.GET.get('titulo', None)
        fecha = request.GET.get('fecha', None)
        pagina = request.GET.get('pagina', 1)

        # Ahora obtenemos todos los eventos y luego filtramos según tenga o no los parámetros de título o fecha
        eventos = Evento.objects.all().order_by('-fecha_hora')  # Ordenados por fecha descendente
        if titulo:
            eventos = eventos.filter(titulo__icontains=titulo)
        if fecha:
            eventos = eventos.filter(fecha_hora__date=fecha)

        # Paginamos máximo 5 elementos por página
        paginator = Paginator(eventos, 5)
        try:
            eventos_paginados = paginator.page(pagina)
        except Exception:
            return JsonResponse({"error": "Página no válida"}, status=400)

        # Ahora que hemos filtrado (o no) construimos el JSON y lo devolvemos
        data = {
            "total_paginas": paginator.num_pages,
            "pagina_actual": eventos_paginados.number,
            "eventos": [
                {
                    "id": e.id,
                    "titulo": e.titulo,
                    "descripcion": e.descripcion,
                    "fecha": e.fecha_hora,
                    "capacidad": e.capacidad_maxima,
                    "imagen_url": e.imagen_url,
                    "organizador": {
                        'id': e.organizador.id,
                        'username': e.organizador.username,
                        'role': e.organizador.role,
                        'bio': e.organizador.bio,
                    },
                } for e in eventos],
        }
        return JsonResponse(data, safe=False)


# POST crear un evento
@csrf_exempt
def crear_evento(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Debes iniciar sesión para crear un evento."}, status=403)

        if request.user.role != "organizador":
            return JsonResponse({"error": "Solo los organizadores pueden crear eventos."}, status=403)

        try:
            data = json.loads(request.body)
            evento = Evento.objects.create(
                titulo=data["titulo"],
                descripcion=data["descripcion"],
                fecha_hora=data["fecha_hora"],
                capacidad_maxima=data["capacidad_maxima"],
                imagen_url=data["imagen_url"],
                organizador=request.user
            )
            return JsonResponse({"id": evento.id, "mensaje": "Evento creado correctamente"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido."}, status=400)

    return JsonResponse({"error": "Método no permitido. Usa POST."}, status=405)


# PUT/PATCH actualizar un evento (sólo organizadores)
@csrf_exempt
@login_required
def actualizar_evento(request, id):
    if request.method in ["PUT", "PATCH"]:
        try:
            data = json.loads(request.body)
            evento = Evento.objects.get(id=id)

            # Verificar si el usuario tiene el rol de organizador
            if request.user.role != "organizador":
                return JsonResponse(
                    {"error": "¡Sólo los organizadores pueden actualizar un evento!"},
                    status=403
                )

            # Actualizar los campos del evento
            evento.titulo = data.get("titulo", evento.titulo)
            evento.descripcion = data.get("descripcion", evento.descripcion)
            evento.fecha_hora = data.get("fecha_hora", evento.fecha_hora)
            evento.capacidad_maxima = data.get("capacidad_maxima", evento.capacidad_maxima)
            evento.imagen_url = data.get("imagen_url", evento.imagen_url)
            evento.save()
            return JsonResponse({"mensaje": "Evento actualizado correctamente"})

        except Evento.DoesNotExist:
            return JsonResponse({"error": "El evento no existe"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido"}, status=400)

    return JsonResponse({"error": "Método no permitido. Usa PUT o PATCH."}, status=405)


# DELETE eliminar un evento (sólo organizadores)
@csrf_exempt
@login_required
def eliminar_evento(request, id):
    if request.method == "DELETE":
        try:
            evento = Evento.objects.get(id=id)

            # Si no es un organizador lo echamos pa fuera
            if request.user.role != "organizador":
                return JsonResponse(
                    {"error": "¡Sólo los organizadores pueden actualizar un evento!"},
                    status=403
                )

            evento.delete()
            return JsonResponse({"mensaje": "Evento eliminado"})

        except Evento.DoesNotExist:
            return JsonResponse({"error": "El evento no existe"}, status=404)

    return JsonResponse({"error": "Método no permitido. Usa DELETE."}, status=405)


# CRUD de reservas:
@login_required
def listar_reservas(request):
    if request.method == "GET":
        reservas = Reserva.objects.filter(usuario=request.user)
        data = [
            {
                "id": reserva.id,
                "evento": {
                    "id": reserva.evento.id,
                    "titulo": reserva.evento.titulo,
                },
                "entradas_reservadas": reserva.entradas_reservadas,
                "estado": reserva.estado,
            } for reserva in reservas
        ]
        return JsonResponse(data, safe=False)

    return JsonResponse({"error": "Método no permitido. Usa GET."}, status=405)


@csrf_exempt
@login_required
def crear_reserva(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            evento = Evento.objects.get(id=data["evento_id"])
            entradas_reservadas = data["entradas_reservadas"]

            reserva = Reserva.objects.create(
                usuario=request.user,
                evento=evento,
                entradas_reservadas=entradas_reservadas,
                estado="pendiente"
            )
            return JsonResponse({"id": reserva.id, "mensaje": "Reserva creada correctamente"})

        except Evento.DoesNotExist:
            return JsonResponse({"error": "El evento no existe"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido"}, status=400)

    return JsonResponse({"error": "Método no permitido. Usa POST."}, status=405)


@csrf_exempt
@login_required
def actualizar_reserva(request, id):
    if request.method in ["PUT", "PATCH"]:
        try:
            data = json.loads(request.body)
            reserva = Reserva.objects.get(id=id)

            # Verificar si el usuario tiene el rol de organizador
            if request.user.role != "organizador":
                return JsonResponse(
                    {"error": "¡Sólo los organizadores pueden actualizar el estado de una reserva!"},
                    status=403
                )

            reserva.estado = data.get("estado", reserva.estado)
            reserva.save()
            return JsonResponse({"mensaje": "Estado de la reserva actualizado correctamente"})

        except Reserva.DoesNotExist:
            return JsonResponse({"error": "La reserva no existe"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido"}, status=400)

    return JsonResponse({"error": "Método no permitido. Usa PUT o PATCH."}, status=405)


@csrf_exempt
@login_required
def cancelar_reserva(request, id):
    if request.method == "DELETE":
        try:
            reserva = Reserva.objects.get(id=id)

            # Verificar si el usuario es el propietario de la reserva y tiene el rol de participante
            if request.user != reserva.usuario or request.user.role != "participante":
                return JsonResponse(
                    {"error": "¡Sólo los participantes pueden cancelar sus propias reservas!"},
                    status=403
                )

            reserva.delete()
            return JsonResponse({"mensaje": "Reserva cancelada"})

        except Reserva.DoesNotExist:
            return JsonResponse({"error": "La reserva no existe"}, status=404)

    return JsonResponse({"error": "Método no permitido. Usa DELETE."}, status=405)


# CRUD de comentarios:
def listar_comentarios(request, evento_id):
    if request.method == "GET":
        try:
            evento = Evento.objects.get(id=evento_id)
            comentarios = Comentario.objects.filter(evento=evento)
            data = [
                {
                    "id": comentario.id,
                    "texto": comentario.texto,
                    "usuario": {
                        "id": comentario.usuario.id,
                        "username": comentario.usuario.username,
                    },
                    "fecha_creacion": comentario.fecha_creacion,
                } for comentario in comentarios
            ]
            return JsonResponse(data, safe=False)
        except Evento.DoesNotExist:
            return JsonResponse({"error": "El evento no existe"}, status=404)

    return JsonResponse({"error": "Método no permitido. Usa GET."}, status=405)


@csrf_exempt
@login_required
def crear_comentario(request, evento_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            texto = data.get("texto")
            if not texto:
                return JsonResponse({"error": "El campo 'texto' es obligatorio."}, status=400)

            evento = Evento.objects.get(id=evento_id)
            comentario = Comentario.objects.create(
                texto=texto,
                evento=evento,
                usuario=request.user
            )
            return JsonResponse({"id": comentario.id, "mensaje": "Comentario creado correctamente"})

        except Evento.DoesNotExist:
            return JsonResponse({"error": "El evento no existe"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido"}, status=400)

    return JsonResponse({"error": "Método no permitido. Usa POST."}, status=405)


# ----------------------------------------------------------------
# USUARIO -------------------------------------------------------
@csrf_exempt
def iniciar_sesion(request):
    if request.method == "POST":
        try:
            # Obtener datos del cuerpo de la petición
            data = json.loads(request.body)
            username = data.get("username", "").strip()
            password = data.get("password", "").strip()

            # Validar que se proporcionaron credenciales
            if not username or not password:
                return JsonResponse({"error": "Se requieren usuario y contraseña"}, status=400)

            # Autenticar usuario
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({
                    "mensaje": "Inicio de sesión exitoso",
                    "usuario": {
                        "id": user.id,
                        "username": user.username,
                        "role": user.role,
                    }
                }, status=200)
            else:
                return JsonResponse({"error": "Credenciales incorrectas"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            role = data.get("role", "participante")  # Por defecto
            bio = data.get("bio", "")

            # Validar que no exista el usuario
            if CustomUser.objects.filter(username=username).exists():
                return JsonResponse({"error": "El nombre de usuario ya está en uso"}, status=400)
            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({"error": "El correo ya está registrado"}, status=400)

            # Crear usuario
            user = CustomUser.objects.create(
                username=username,
                email=email,
                password=make_password(password),  # Hashear la contraseña
                role=role,
                bio=bio
            )

            return JsonResponse({
                "mensaje": "Usuario registrado con éxito",
                "usuario": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "bio": user.bio
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)
# ----------------------------------------------------------------

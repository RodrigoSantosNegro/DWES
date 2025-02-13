import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser, Evento, Comentario, Reserva
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt



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


#PUT/PATCH actualizar un evento (sólo organizadores)
@csrf_exempt
def actualizar_evento(request, id):
    if request.method in ["PUT", "PATCH"]:
        try:
            data = json.loads(request.body)
            evento = Evento.objects.get(id=id)

            # Si no es un organizador lo echamos pa fuera
            if request.user != evento.organizador:
                return JsonResponse(
                    {"error": "¡Sólo los organizadores pueden actualizar un evento pillo!"},
                    status=403
                )

            evento.titulo = data.get("titulo", evento.titulo)
            evento.descripcion = data.get("descripcion", evento.descripcion)
            evento.capacidad_maxima = data.get("capacidad_maxima", evento.capacidad_maxima)
            evento.imagen_url = data.get("imagen_url", evento.imagen_url)
            evento.save()
            return JsonResponse({"mensaje": "Evento actualizado"})

        except Evento.DoesNotExist:
            return JsonResponse({"error": "El evento no existe"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "El cuerpo de la solicitud no es un JSON válido"}, status=400)

    return JsonResponse({"error": "Método no permitido. Usa PUT o PATCH."}, status=405)
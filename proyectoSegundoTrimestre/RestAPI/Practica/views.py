import json

from django.shortcuts import render
from django.http import JsonResponse
from models import CustomUser, Evento, Comentario, Reserva
from django.core.paginator import Paginator

# Create your views here.

# CRUD DE EVENTOS -----------------------------------------------
#GET lista de eventos dispoñibles
def listar_eventos(request):
    titulo = request.GET.get('titulo', None)
    fecha = request.GET.get('fecha', None)
    pagina = request.GET.get('pagina', 1)

    #Ahora obtenemos todos los eventos y luego filtramos según tenga o no los parámetros de título o fecha
    eventos = Evento.objects.all().order_by('-fecha_hora') #Ordenados por fecha descendente
    if titulo:
        eventos = eventos.filter(titulo__icontains=titulo)
    if fecha:
        eventos = eventos.filter(fecha_hora__date=fecha)


    #Paginamos máximo 5 elementos por página
    paginator = Paginator(eventos, 5)
    try:
        eventos_paginados = paginator.page(pagina)
    except Exception:
        return JsonResponse({"error": "Página no válida"}, status=400)


    #Ahora que hemos filtrado (o no) construimos el JSON y lo devolvemos
    data = {
        "total_paginas": paginator.num_pages,
        "pagina_actual": eventos_paginados.number,
        "eventos":[
            {
                "id": e.id,
                "titulo": e.titulo,
                "descripcion": e.descripcion,
                "fecha": e.fecha_hora,
                "capacidad": e.capacidad_maxima,
                "imagen_url": e.imagen_url,
                "organizador":e.organizador
             } for e in eventos],
    }
    return JsonResponse(data, safe=False)

#POST crear un evento
def crearEvento(request):

    #ME FALTA PONER QUE SÓLO LOS ORGANIZADORES PUEDAN HACER ESTO
    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


    if request.method == "POST":
        data = json.loads(request.body)
        evento = Evento.objects.create(
            titulo = data["titulo"],
            descripcion = data["descripcion"],
            fecha_hora = data["fecha_hora"],
            capacidad_maxima = data["capacidad_maxima"],
            imagen_url = data["imagen_url"],
            organizador= data["organizador"]
        )
        return JsonResponse({"id": evento.id, "mensaje": "Evento creado correctamente"})

#PUT/PATCH actualizar un evento (sólo organizadores)


#DELETE eliminar un evento (sólo organizadores)


#----------------------------------------------------------------
# GESTIÓN DE RESERVAS -------------------------------------------
#GET Listar reservas de un usuario autenticado

#POST crear nueva reserva

#PUT/PATCH Actualizar el estado de una reserva (solo organizadores).

#DELETE Cancelar una reserva (solo participantes para sus reservas).

#----------------------------------------------------------------
# COMENTARIOS ---------------------------------------------------
#GET Listar comentarios de un evento.
#POST Crear un comentario asociado a un evento (solo usuarios autenticados).

#----------------------------------------------------------------
# USUARIO -------------------------------------------------------

#----------------------------------------------------------------
from django.shortcuts import render
from django.http import JsonResponse
from models import CustomUser, Evento, Comentario, Reserva
from django.core.paginator import Paginator


# Create your views here.

#CRUD de eventos:
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


#Gestión de reservas:
def listar_reservas(request):
    if(request.method == 'GET'):

        reservas = Reserva.objects.all()

        data = [
            {
                "id": r.id,
                "usuario": r.usuario,
                "evento": r.evento,
                "entradas reservadas": r.entradas_reservadas,
                "estado": r.estado,
            } for r in reservas
        ]
        return JsonResponse(data, safe=False)


@crsf_excempt
def crear_reserva(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        reserva = Reserva.objects.create(
            usuario = data["usuario"],
            evento = data["evento"],
            entradas_reservadas = data["entradas_reservadas"],
            estado = data["estado"]
        )
        return JsonResponse({"id": reserva.id, "mensaje":"Reserva creada correctamente"})

@csrf_exempt
def actualizar_estado_reserva(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        reserva = Reserva.objects.get(id=id)

        if reserva.organizador != request.user:
            return JsonResponse({"error":"Pillueeelo que sólo los organizadores pueden cambiar el estado de la reserva"}, status=403)

        reserva.estado = data.get("estado", reserva.estado)
        reserva.save()

        return JsonResponse({"mensaje": "Estado de la reserva actualizado"})


def cancelar_reserva(request, id):
    if(request.method == 'DELETE'):
        reserva = Reserva.objects.get(id=id)

        if():
            return JsonResponse({"error":"No hay ninguna reserva que cancelar para este usaurio"})


#Comentarios:
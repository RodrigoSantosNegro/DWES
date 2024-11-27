from django.http import JsonResponse
from .models import Tlibros
from .models import Tcomentarios
import json


def obtener_libros(request):
    libros = Tlibros.objects.all()
    respuesta = []
    for libro in libros:
        respuesta.append({
            'id': libro.id,
            'nombre': libro.nombre,
            'autor': libro.autor,
            'año_publicacion': libro.año_publicacion,
            'url_imagen': libro.url_imagen,
        })
    return JsonResponse(respuesta, safe=False)


def obtener_libro_por_id(request, id):
    try:
        libro = Tlibros.objects.get(id=id)
        comentarios = Tcomentarios.objects.filter(libro=libro)
        comentarios_data = [{'id': c.id, 'comentario': c.comentario, 'fecha': c.fecha} for c in comentarios]
        respuesta = {
            'id': libro.id,
            'nombre': libro.nombre,
            'autor': libro.autor,
            'año_publicacion': libro.año_publicacion,
            'url_imagen': libro.url_imagen,
            'comentarios': comentarios_data,
        }
        return JsonResponse(respuesta, safe=False)
    except Tlibros.DoesNotExist:
        return JsonResponse({'error': 'Libro no encontrado'}, status=404)

@csrf_excempt
def crear_comentario(request, id):
    if request.method == 'POST':
        try:
            libro = Tlibros.objects.get(id=id)
            data = json.loads(request.body)
            nuevo_comentario = Tcomentarios(libro=libro, comentario=data.get('nuevo_comentario'))
            nuevo_comentario.save()
            return JsonResponse({}, status=200)
        except Tlibros.DoesNotExist:
            return JsonResponse({'error': 'Libro no encontrado'}, status=404)
        except KeyError:
            return JsonResponse({'error': 'Falta el campo "nuevo_comentario"'}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

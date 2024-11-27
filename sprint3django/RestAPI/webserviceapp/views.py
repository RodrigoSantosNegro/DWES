from django.http import JsonResponse
from .models import Tlibros
from .models import Tcomentarios

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

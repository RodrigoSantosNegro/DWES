from django.http import JsonResponse
from .models import Tlibros


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

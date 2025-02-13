from django.contrib import admin
from .models import CustomUser, Evento, Reserva, Comentario

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Evento)
admin.site.register(Reserva)
admin.site.register(Comentario)
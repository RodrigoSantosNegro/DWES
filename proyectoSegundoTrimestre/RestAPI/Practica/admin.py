from django.contrib import admin
from .models import Evento, CustomUser, Comentario, Reserva

# Register your models here.
admin.site.register(Evento)
admin.site.register(CustomUser)
admin.site.register(Comentario)
admin.site.register(Reserva)

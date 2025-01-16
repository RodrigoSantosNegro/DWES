from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('organizador', 'Organizador'),
        ('participante', 'Participante'),
    ]

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='participante')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    capacidad_maxima = models.PositiveIntegerField()
    imagen_url = models.URLField(blank=True, null=True)
    organizador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="eventos", limit_choices_to={'role': 'organizador'})

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reservas", limit_choices_to={'role': 'participante'})
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="reservas")
    entradas_reservadas = models.PositiveIntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.evento.titulo}"
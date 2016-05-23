from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Cases(models.Model):
    localitat = models.CharField(max_length=200)
    adressa = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.localitat

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Persona(models.Model):
    cognoms = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    btc_address = models.CharField(max_length=34, null=True)
    id_casa = models.ForeignKey(Cases, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

"""
class Login(models.Model):
    usuari = models.CharField(max_length=100)
    contrassenya = models.CharField(max_length=100)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuari
"""

class Xat(models.Model):
    date_sent = models.DateTimeField(auto_now_add=True)
    #user = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    text = models.CharField(max_length=100)
    #id_usuari = models.ForeignKey(Login, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class NotaCalendario(models.Model):
    dateField = models.DateField(auto_now_add=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nota = models.CharField(max_length=2000)

    def __str__(self):
        return self.nota

class Factura(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    image = models.ImageField()
    preu = models.FloatField()
    def __str__(self):
        return str(self.preu)
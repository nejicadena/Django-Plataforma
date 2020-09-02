from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    nombre = models.CharField(null=True, blank=True, max_length=50)
    apellido = models.CharField(null=True, blank=True, max_length=50)
    fecha = models.DateField(null=True, blank=True)
    direcccion = models.TextField(null=True, blank=True)
    

    class Meta:
        ordering = ['user__username']


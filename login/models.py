from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import os
# Create your models here.



    



class Veterinaria(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    numerovet = PhoneNumberField(blank=True,null=True,unique = True)
    nombrevet = models.CharField(max_length=100,null=True)
    direccionvet = models.CharField(max_length=100,null=True)
    correovet = models.EmailField(blank=True,null=True,unique=True)
    schedule_open = models.TimeField(blank=True,null=True)
    schedule_close = models.TimeField(blank=True,null=True)

    def __str__(self):
        return self.user

class Cliente(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    correo = models.EmailField(max_length=100,null=True,blank=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    vet = models.ForeignKey(Veterinaria,on_delete=models.DO_NOTHING,null=True,blank=True) 
# Campos que se llenan al sincronizar con la mascota    
    numerovet = PhoneNumberField(blank=True,null=True)
    nombrevet = models.CharField(max_length=100,null=True)
    direccionvet = models.CharField(max_length=100,null=True)
    correovet = models.EmailField(blank=True,null=True)
    schedule_open = models.TimeField(blank=True,null=True)
    schedule_close = models.TimeField(blank=True,null=True)
    def __str__(self):
        return self.user
    

    
    



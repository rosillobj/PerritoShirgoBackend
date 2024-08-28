from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from login.models import Cliente
import os

def get_upload_path6(instance, filename):
    """Función que devuelve la ruta donde se almacenará la imagen."""
    # En este ejemplo, usaremos el ID del perrito como nombre de carpeta
    # y el nombre del archivo original como nombre del archivo.
    return os.path.join('perritosfotos', f'{instance.id_perritos}{instance.perrito}', filename)
def get_upload_path(instance, filename):
    """Función que devuelve la ruta donde se almacenará la imagen."""
    # En este ejemplo, usaremos el ID de la tienda como nombre de carpeta
    # y un nombre fijo para el archivo.
    folder_path = os.path.join('perritosfotos', f'{instance.id_perritos}{instance.perrito}')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Obtener una lista de archivos en la carpeta
    files = os.listdir(folder_path)
    # Si hay un archivo existente, eliminarlo
    if len(files) > 0:
        for file in files:
            os.remove(os.path.join(folder_path, file))
    # Devolver la ruta para la nueva imagen
    return os.path.join(folder_path, 'imagen4.jpg')
def get_upload_path2(instance, filename):
    """Función que devuelve la ruta donde se almacenará la imagen."""
    # En este ejemplo, usaremos el ID de la tienda como nombre de carpeta
    # y un nombre fijo para el archivo.
    folder_path = os.path.join('productos', f'{instance.numerovet}', f'{instance.title}')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Obtener una lista de archivos en la carpeta
    files = os.listdir(folder_path)
    # Si hay un archivo existente, eliminarlo
    if len(files) > 0:
        for file in files:
            os.remove(os.path.join(folder_path, file))
    # Devolver la ruta para la nueva imagen
    return os.path.join(folder_path, 'imagen.jpg')
def get_upload_path3(instance, filename):
    """Función que devuelve la ruta donde se almacenará la imagen."""
    # En este ejemplo, usaremos el ID de la tienda como nombre de carpeta
    # y un nombre fijo para el archivo.
    folder_path = os.path.join('Tiendas', f'tienda{instance.numerovet}')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Obtener una lista de archivos en la carpeta
    files = os.listdir(folder_path)
    # Si hay un archivo existente, eliminarlo
    if len(files) > 0:
        for file in files:
            os.remove(os.path.join(folder_path, file))
    # Devolver la ruta para la nueva imagen
    return os.path.join(folder_path, 'imagen.jpg')
def get_upload_path4(instance, filename):
    """Función que devuelve la ruta donde se almacenará la imagen."""
    # En este ejemplo, usaremos el ID de la tienda como nombre de carpeta
    # y un nombre fijo para el archivo.
    folder_path = os.path.join('Tiendas2',f'tienda{instance.numerovet}')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Obtener una lista de archivos en la carpeta
    files = os.listdir(folder_path)
    # Si hay un archivo existente, eliminarlo
    if len(files) > 0:
        for file in files:
            os.remove(os.path.join(folder_path, file))
    # Devolver la ruta para la nueva imagen
    return os.path.join(folder_path, 'imagen2.jpg')
def get_upload_path7(instance, filename):
    """Función que devuelve la ruta donde se almacenará la imagen."""
    # En este ejemplo, usaremos el ID de la tienda como nombre de carpeta
    # y un nombre fijo para el archivo.
    folder_path = os.path.join('Expedientes',f'tienda{instance.id}')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Obtener una lista de archivos en la carpeta
    files = os.listdir(folder_path)
    # Si hay un archivo existente, eliminarlo
    if len(files) > 0:
        for file in files:
            os.remove(os.path.join(folder_path, file))
    # Devolver la ruta para la nueva imagen
    return os.path.join(folder_path, 'imagen2.jpg')

class PerritosSh3(models.Model):

    id_perritos=models.AutoField(primary_key=True)
    id_vet=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    id_cliente=models.ForeignKey(Cliente,on_delete=models.DO_NOTHING, blank=True,null=True)
    numerodueno = PhoneNumberField(blank=True,null=True)
    perrito=models.CharField(max_length=200)
    edad = models.CharField(max_length=2,null=True)
    genero = models.CharField(max_length=50)
    especie = models.CharField(max_length=50,null=True)
    raza = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True,upload_to=get_upload_path)
    nombredueno = models.CharField(max_length=100 ,null=True)






    def __str__(self):
        return self.id_perritos
class PerritossSh2(models.Model):


    id_perritos=models.AutoField(primary_key=True)
    id_perritos2 = models.OneToOneField(PerritosSh3,on_delete=models.CASCADE,null=True,blank=True)
    id_vet=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,blank=True)
    id_cliente=models.ForeignKey(Cliente,on_delete=models.DO_NOTHING, blank=True,null=True)
 
    numerodueno = PhoneNumberField(blank=True,null=True)
    perrito=models.CharField(max_length=200)
    edad = models.CharField(max_length=2,null=True)
    genero = models.CharField(max_length=50)
    especie = models.CharField(max_length=50,null=True)
    raza = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True,upload_to=get_upload_path)
    nombredueno = models.CharField(max_length=100 ,null=True)




    def __str__(self):
        return self.id_perritos    

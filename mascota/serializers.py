from .models import PerritossSh2,PerritosSh3
from rest_framework.serializers import ModelSerializer


class MascotaSerializer(ModelSerializer):
    
    class Meta:
        
        model = PerritosSh3
        fields = ['id_vet','numerodueno','nombredueno','perrito','edad','genero','especie','raza']

    
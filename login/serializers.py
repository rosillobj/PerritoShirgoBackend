from rest_framework.serializers import ModelSerializer
from .models import Veterinaria,Cliente
from django.contrib.auth.models import User


class VeterinariaSerializer(ModelSerializer):
    
    class Meta:
        
        model = Veterinaria
        fields = ['id','numerovet','nombrevet','direccionvet','correovet','schedule_open','schedule_close']
    def create(self, validated_data):
        
        return super().create(validated_data)
    


class ClienteSerializer(ModelSerializer):
    
    class Meta:
        
        model = Cliente
        fields = ['location','created_at','updated_at',]



            
class UserClienteSerializer(ModelSerializer):
   

    class Meta:
        model = User
        fields = ['id', 'username', 'password','first_name','last_name','phonenumber','email']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self,validated_data):
        
        

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=validated_data.get('is_staff', False),
            is_vet=validated_data.get('is_vet', False),
            last_name=validated_data['last_name'],
            first_name=validated_data['first_name'],
            phonenumber=validated_data['phonenumber'],
            email = validated_data['email'],
            )
    
    # Crear la instancia de Cliente asociada al usuario

        return user
        
class UserVeterinariaSerializer(ModelSerializer):
   

    class Meta:
        model = User
        fields = ['id', 'username', 'password','last_name','first_name','email','phonenumber']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
     
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=validated_data.get('is_staff', False),
            is_vet = validated_data.get('is_vet',True),
            last_name = validated_data['last_name'],
            first_name = validated_data['first_name'],
            phonenumber = validated_data['phonenumber'],
            email = validated_data['email'],
                         
        )
        
        return user         
        
        
    



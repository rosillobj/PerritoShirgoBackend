from django.shortcuts import render
from .serializers import UserClienteSerializer,UserVeterinariaSerializer,VeterinariaSerializer,ClienteSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView,CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.


class UserViewRegister(CreateAPIView):
    
   
    serializer_class = UserClienteSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
        else:
            print (serializer.errors)
        return super().create(request, *args, **kwargs)

    

class UserVeterinariaViewRegister(CreateAPIView):
    
   
    serializer_class = UserVeterinariaSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
        else:
            print (serializer.errors)
        return super().create(request, *args, **kwargs)


    
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import MascotaSerializer
from .models import PerritosSh3, PerritossSh2
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated




class MascotaRegisterView(generics.CreateAPIView):
    
    serializer_class = MascotaSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        
        if serializer.is_valid():
            serializer.save(id_vet = self.request.user)
        else :
            print(serializer.errors)
        
        return super().perform_create(serializer)
    





from rest_framework import generics
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Note

class NoteView(generics.ListCreateAPIView):
    
    
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        note = Note.objects.filter(author = user)
        return note
    
    def perform_create(self, serializer):
        print("havber que trae",serializer.validated_data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDeleteView(generics.DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        user=self.request.user
        note = Note.objects.filter(author = user)
        return note

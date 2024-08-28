from django.urls import path,include
from . import views




urlpatterns = [
    
    path("notes/", views.NoteView.as_view(),name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDeleteView.as_view(),name="delete-note"),

    
]
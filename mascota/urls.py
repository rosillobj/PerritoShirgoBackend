from. import views
from django.urls import path



urlpatterns = [
    path("mascota/",views.MascotaRegisterView.as_view(),name="mascota"),
    
]
from django.urls import path
from . import views

app_name = "publicaciones"

urlpatterns = [
    # URL: "" -> Vista: InicioView -> Nombre: "inicio"
    path("", views.InicioView.as_view(), name="inicio"),
    
    # URL: "publicaciones/" -> Vista: PublicacionListView -> Nombre: "lista_publicaciones"
    path("publicaciones/", views.PublicacionListView.as_view(), name="lista_publicaciones"),
    
    # URL: "publicaciones/<int:publicacion_id>/" -> Vista: PublicacionDetailView -> Nombre: "detalle_publicacion"
    path("publicaciones/<int:publicacion_id>/", views.PublicacionDetailView.as_view(), name="detalle_publicacion"),
]
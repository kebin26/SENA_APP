from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('programas/', views.ProgramaListView.as_view(), name='lista_programas'),
    path('programas/editar<int:pk>/', views.ProgramaDetailView.as_view(), name='editar_programa'),
    path('programas/eliminar/<int:pk>/', views.ProgramaDetailView.as_view(), name='eliminar_programa'),
    #path('crear_programa/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('crear_programa/', views.crear_programa, name='crear_programa'),
]
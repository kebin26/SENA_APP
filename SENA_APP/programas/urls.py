from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('programas/', views.ProgramaListView.as_view(), name='lista_programas'),
    path('programas/<int:pk>/', views.ProgramaDetailView.as_view(), name='detalle_programa'),
    #path('crear_programa/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('crear_programa/', views.crear_programa, name='crear_programa'),
]
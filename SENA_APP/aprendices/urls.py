from django.urls import path
from . import views

urlpatterns = [
    path('', views.aprendices, name='lista_aprendices'),
    
]

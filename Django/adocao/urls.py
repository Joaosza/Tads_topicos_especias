#Modulo do Django para criar urls
from django.urls import path
#IMporte todas suas classes do views.py
from .views import *

urlpatterns = [
    #patch('caminho/da/url', ClasseDoview.as_view(),name="NomeDessaUrl")
    path('inicio/', PaginaInicialView.as_view(), name="index"),
    path('sobre/', PaginaInicialSobreView.as_view(), name="sobre"),
]

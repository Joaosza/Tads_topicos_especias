from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here  .
class PaginaInicialView(TemplateView):
    #Nome do arquivo que vai ser utilizado para renderizar esta pagina/metodo/classe
    template_name  = "index.html"

class PaginaInicialSobreView(TemplateView):
    template_name  = "sobre.html"

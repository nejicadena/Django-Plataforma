from django.shortcuts import render
from django.views.generic.base import TemplateView 

# Create your views here.

class colePageView(TemplateView):
    template_name = 'mc/colectivo.html'
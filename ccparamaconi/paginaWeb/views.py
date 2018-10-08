from django.shortcuts import render
from django.views.generic import DetailView
from paginaWeb.models import inicio

class IndexView(DetailView):
    model = inicio,
    template_name = 'paginaWeb/index.html',

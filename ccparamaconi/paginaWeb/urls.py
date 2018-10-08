from paginaWeb.views import IndexView
from django.urls import path

app_name = 'paginaWeb'

urlpatterns = [
    path('index/', IndexView.as_view(), name="inicio")


]
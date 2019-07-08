from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'answer', views.answer, name='answer'),
    path(r'grafico', views.grafico, name='grafico'),
    path(r'api/grafico', views.apigrafico, name="graficos"),
    path(r'api/curso', views.apicurso, name="graficos"),
    path(r'api/campus', views.apicampus, name="graficos")
]


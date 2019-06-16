from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('answer', views.answer, name='answer'),
    path('grafico', views.grafico, name='grafico'),
    path('api/grafico', views.apigrafico, name="graficos"),
    path('api/curso', views.apicurso, name="graficos"),
    path('api/campus', views.apicampus, name="graficos")
]


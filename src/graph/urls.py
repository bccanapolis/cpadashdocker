from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r's4UkHMQC', views.answer, name='answerestudante'),
    path(r'zc3WsGum', views.answer, name='answerdocente'),
    path(r'4jn7qduk', views.answer, name='answerreitoria'),
    path(r'g3YTAfpT', views.answer, name='answercampus'),
    path(r'v1/pergunta', views.apianswer, name="apianswer"),
    path(r'v1/grafico', views.apigrafico, name="graficos"),
    path(r'v1/curso', views.apicurso, name="graficos"),
    path(r'v1/campus', views.apicampus, name="campus"),
    path(r'v1/atuacao', views.apiatuacao, name="atuacao"),
    path(r'v1/lotacao', views.apilotacao, name="lotacao"),
    path(r'v1/segmento', views.apisegmento, name="segmento"),
    path(r'v1/ano', views.apiano, name="ano"),
]

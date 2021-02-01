from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    # path(r's4UkHMQC', views.answer, name='answerestudante'),
    # path(r'zc3WsGum', views.answer, name='answerdocente'),
    # path(r'4jn7qduk', views.answer, name='answerreitoria'),
    # path(r'g3YTAfpT', views.answer, name='answercampus'),
    path(r'v1/resposta', views.apianswer, name="resposta"),
    path(r'v1/grafico', views.apigrafico, name="graficos"),
    path(r'v1/curso', views.apicurso, name="curso"),
    path(r'v1/campus', views.apicampus, name="campus"),
    path(r'v1/atuacao', views.apiatuacao, name="atuacao"),
    path(r'v1/lotacao', views.apilotacao, name="lotacao"),
    path(r'v1/segmento', views.apisegmento, name="segmento"),
    path(r'v1/ano', views.apiano, name="ano"),
    path(r'v1/eixo', views.apieixo, name="eixo"),
    path(r'v1/update', views.apiupdate, name="update"),
    path(r'v1/pergunta', views.apipergunta, name="pergunta"),
    path(r'v1/dimensao', views.apidimensao, name="dimensao"),
]

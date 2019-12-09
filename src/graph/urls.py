from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.grafico, name='index'),
    # path(r's4UkHMQC', views.answer, name='answerestudante'),
    # path(r'zc3WsGum', views.answer, name='answerdocente'),
    # path(r'4jn7qduk', views.answer, name='answerreitoria'),
    # path(r'g3YTAfpT', views.answer, name='answercampus'),
    path(r'QthDtt4r', views.grafico, name='grafico'),
    path(r'api/answer', views.apianswer, name="apianswer"),
    path(r'api/grafico', views.apigrafico, name="graficos"),
    path(r'api/curso', views.apicurso, name="graficos"),
    path(r'api/campus', views.apicampus, name="campus"),
    path(r'api/atuacao', views.apiatuacao, name="atuacao"),
    path(r'api/lotacao', views.apilotacao, name="lotacao"),
    path(r'api/segmento', views.apisegmento, name="segmento"),
    path(r'api/info', views.apiinfo, name="info"),
]

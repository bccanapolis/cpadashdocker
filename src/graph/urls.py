from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r's4UkHMQC', views.answer, name='answerestudante'),
    path(r'zc3WsGum', views.answer, name='answerdocente'),
    path(r'4jn7qduk', views.answer, name='answerreitoria'),
    path(r'g3YTAfpT', views.answer, name='answercampus'),
    path('obrigado', views.obrigado, name='obrigado'),
    path(r'grafico', views.grafico, name='grafico'),
    path(r'api/grafico', views.apigrafico, name="graficos"),
    path(r'api/curso', views.apicurso, name="graficos"),
    path(r'api/campus', views.apicampus, name="graficos"),
    path(r'api/atuacao', views.apiatuacao, name="atuacao"),
    path(r'api/lotacao', views.apilotacao, name="lotacao"),
]


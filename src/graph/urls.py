from django.urls import path
from . import views
from .authenticated import views as auth
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'admin/auth/user', auth.AuthView.as_view(), name='auth_user'),
    path(r'admin/auth/login', obtain_auth_token, name='auth_token'),
    path(r'admin/me', auth.UserView.as_view(), name='auth_user'),
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
    path(r'v1/relatorio', views.apirelatorio, name="relatorio"),
]

import os

from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from .models import Campus, Segmento, Curso, Pergunta, ParticipacaoPergunta, Grafico, RespostaObjetiva, CursoCampus, Atuacao, Lotacao
from .database import *
import json
from django.http import JsonResponse

def obrigado(request):
    return render(request, "thanks.html ")

def index(request):
    return render(request, "graph/index.html")

def answer(request):
    segmento = ''
    if request.path == "/s4UkHMQC":
        segmento = "Estudante"
    elif request.path == "/zc3WsGum":
        segmento = "Docente"
    elif request.path == "/g3YTAfpT":
        segmento = "Técnico Administrativo Câmpus"
    elif request.path == "/4jn7qduk":
        segmento = "Técnico Administrativo Reitoria"



    if request.method == "GET":
        lotacao = request.GET.get("lotacao")
        cursos = json.dumps(list(Curso.objects.all().order_by(
            "nome").values('id', 'nome')))

        tiposPessoa = Segmento.objects.all().order_by("-id").values('id', 'nome')
        campuses = Campus.objects.all().order_by('nome').values('id', 'nome')
        perguntas = [{'id': pergunta['id'], 'titulo': pergunta['titulo'], 'tipo': pergunta['tipo'], 'lotacao': pergunta['perguntasegmento__lotacao__titulo']} for pergunta in Pergunta.objects.filter(perguntasegmento__segmento__nome=segmento).order_by("dimensao").order_by("tipo").values('id', 'titulo', 'tipo', 'dimensao', 'perguntasegmento__lotacao__titulo')]
        resp_objetivas = [{'id': pergunta['id'], 'titulo': pergunta['titulo'], 'value': pergunta['value']} for pergunta in RespostaObjetiva.objects.all().order_by("-value").values('id','titulo','value')]
        return render(request, "graph/answer.html", {
            "route": segmento, "cursos": cursos, "tiposPessoa": tiposPessoa, "campus": campuses, "perguntas": perguntas, "resp_objetivas": resp_objetivas
        })
    elif request.method == "POST":
        form = request.POST
        naoaplica = request.POST.get("naoaplica")
        ParticipacaoPergunta.create_participacao(naoaplica=naoaplica, atuacao=form['atuacao'], lotacao=form['lotacao'], segmento=segmento, curso=form['curso'], campus=form['campus'], perguntas=form)
        return HttpResponseRedirect("/")


def grafico(request):
    return render(request, 'graph/grafico.html')

def apiatuacao(request):
    atuacao = [{'id':atuacao['id'], 'nome': atuacao['titulo']} for atuacao in Atuacao.objects.values('id', 'titulo').all()]
    return JsonResponse({"atuacao": atuacao})

def apilotacao(request):
    lotacao = [{'id':lotacao['id'], 'nome': lotacao['titulo']} for lotacao in Lotacao.objects.values('id', 'titulo').all()]
    return JsonResponse({"lotacao": lotacao})

def apicurso(request):
    campus = request.GET.get("campus")
    grafico = request.GET.get("grafico")
    cursos = [{'id':curso['id'], 'nome': curso['nome'] } for curso in Curso.objects.filter(cursocampus__campus_id=campus).exclude(nome='Não Aplica').order_by('nome').values('nome', 'id')]
    return JsonResponse({"cursos": cursos})


# def apicampus(request):
#     grafico = request.GET.get("grafico")
#     print(grafico)
#     # cur.execute('select distinct campus, campus_id from graph_view{} order by campus;'.format(int(grafico)))
#     campus = []
#     return JsonResponse({'campus': campus})


# def apigrafico(request):
#     db_view = request.GET.get("view")
#     query_campus = request.GET.get('campus')
#     query_curso = request.GET.get('curso')
#     data = []
#
#     if db_view == None:
#         graficos = [{'id': grafico['id'], 'numero':grafico['numero'], 'titulo':grafico['titulo']}
#                     for grafico in Grafico.objects.values('id', 'titulo', 'numero').order_by('numero')]
#         return JsonResponse({'graficos': graficos})
#
#     grafico = [{'id': grafico['id'], 'titulo':grafico['titulo'], 'numero':grafico['numero']}
#                for grafico in Grafico.objects.values('id', 'titulo', 'numero').filter(numero=db_view)]
#     if db_view == '1':
#         sql = list(fetch_view1(query_campus))
#         print(sql)
#         for row in range(0, len(sql)):
#             if(query_campus == '0'):
#                 data.append({'count': sql[row][0], 'campus': sql[row][1]})
#             else:
#                 data.append({'count': sql[row][0], 'campus': sql[row][1],'curso':sql[row][2]})
#     else:
#         sql = list(fetch_view(db_view, query_campus, query_curso))
#         for row in range(0, len(sql)):
#             data.append(
#                 {'count': sql[row][0], 'resposta': sql[row][1], 'segmento': sql[row][2]})
#     return JsonResponse(dict(data=data, grafico=grafico))
#

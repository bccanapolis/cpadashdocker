import os

from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from .models import Campus, Segmento, Curso, Pergunta, ParticipacaoPergunta, Grafico, RespostaObjetiva
from .database import *
import json
from django.http import JsonResponse
import psycopg2 as psy

con = psy.connect(
    database=os.getenv('DATABASE_NAME', 'cpadash'),
    user='postgres',
    password=os.getenv('DATABASE_PASS', 'cpadash#2019'),
    host=os.getenv('DATABASE_HOST', 'localhost'),
    port=os.getenv('DATABASE_PORT', 5432),
)

cur = con.cursor()

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
    return render(request, 'graph/../templates/grafico.html')

def apiatuacao(request):
    atuacao = []
    cur.execute('select id, titulo from graph_atuacao')
    for i in cur.fetchall():
        atuacao.append({'id': i[0], 'nome': i[1]})
    return JsonResponse({"atuacao": atuacao})

def apilotacao(request):
    lotacao = []
    cur.execute('select id, titulo from graph_lotacao')
    for i in cur.fetchall():
        lotacao.append({'id': i[0], 'nome': i[1]})
    return JsonResponse({"lotacao": lotacao})

def apicurso(request):
    campus = request.GET.get("campus")
    grafico = request.GET.get("grafico")
    cursos = []
    if int(grafico) == 0 or grafico == None:
        cur.execute('select graph_curso.nome as nome, graph_curso.id as curso_id from graph_curso left join graph_cursocampus on graph_curso.id = graph_cursocampus.curso_id left join  graph_campus on graph_cursocampus.campus_id = graph_campus.id where graph_campus.id = {} and graph_curso.nome != \'Não Aplica\' order by nome'.format(campus))
        for i in cur.fetchall():
            cursos.append({'id': i[1], 'nome': i[0]})

    if int(grafico) > 1:
        cur.execute('select distinct curso, curso_id from graph_view{} where campus_id = {} order by curso;'.format(grafico, campus))
        for i in cur.fetchall():
            cursos.append({'id': i[1], 'nome': i[0]})
    return JsonResponse({"cursos": cursos})


def apicampus(request):
    grafico = request.GET.get("grafico")
    print(grafico)
    cur.execute('select distinct campus, campus_id from graph_view{} order by campus;'.format(int(grafico)))
    campus = []
    for i in cur.fetchall():
        campus.append({'id': i[1], 'nome':i[0]});

    return JsonResponse({'campus': campus})


def apigrafico(request):
    db_view = request.GET.get("view")
    query_campus = request.GET.get('campus')
    query_curso = request.GET.get('curso')
    data = []

    if db_view == None:
        graficos = [{'id': grafico['id'], 'numero':grafico['numero'], 'titulo':grafico['titulo']}
                    for grafico in Grafico.objects.values('id', 'titulo', 'numero').order_by('numero')]
        return JsonResponse({'graficos': graficos})

    grafico = [{'id': grafico['id'], 'titulo':grafico['titulo'], 'numero':grafico['numero']}
               for grafico in Grafico.objects.values('id', 'titulo', 'numero').filter(numero=db_view)]
    if db_view == '1':
        sql = list(fetch_view1(query_campus))
        print(sql)
        for row in range(0, len(sql)):
            if(query_campus == '0'):
                data.append({'count': sql[row][0], 'campus': sql[row][1]})
            else:
                data.append({'count': sql[row][0], 'campus': sql[row][1],'curso':sql[row][2]})
    else:
        sql = list(fetch_view(db_view, query_campus, query_curso))
        for row in range(0, len(sql)):
            data.append(
                {'count': sql[row][0], 'resposta': sql[row][1], 'segmento': sql[row][2]})
    return JsonResponse(dict(data=data, grafico=grafico))


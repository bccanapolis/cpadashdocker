from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from .models import Campus, Segmento, Curso, Pergunta, ParticipacaoPergunta, Grafico
from .database import *
import json
from django.http import JsonResponse
import psycopg2 as psy

# con = psy.connect(
#     database='cpadash',
#     user='super_cpadash@cpadash',
#     password='TROLLaudi40)',
#     host='cpadash.postgres.database.azure.com',
#     port=5432,
#     sslmode='require'
# )

con = psy.connect(
    database='cpadash',
    user='postgres',
    password='cpadash2019',
    host='db',
    port=5432,
)

cur = con.cursor()

def index(request):
    return render(request, "graph/index.html")


def answer(request):
    if request.method == "GET":
        cursos = json.dumps(list(Curso.objects.all().order_by(
            "nome").values('id', 'nome', 'campus')))
        tiposPessoa = Segmento.objects.all().order_by("-id").values('id', 'nome')
        campuses = Campus.objects.all().order_by('nome').values('id', 'nome')
        perguntas = [{'id': pergunta['id'], 'titulo': pergunta['titulo']} for pergunta in Pergunta.objects.all().order_by("id").values('id', 'titulo')]

        return render(request, "graph/answer.html", {
            "cursos": cursos, "tiposPessoa": tiposPessoa, "campus": campuses, "perguntas": perguntas
        })
    elif request.method == "POST":
        form = request.POST
        ParticipacaoPergunta.create_participacao(form['nome'], form['segmento'], form['curso'],
                                                 {1: form['resposta-1'], 2: form['resposta-2'], 3: form['resposta-3'],
                                                  4: form['resposta-4'], 5: form['resposta-5'], 6: form['resposta-6'],
                                                  7: form['resposta-7'], 8: form['resposta-8'], 9: form['resposta-9'],
                                                  10: form['resposta-10'], 11: form['resposta-11'],
                                                  12: form['resposta-12'], 13: form['resposta-13'],
                                                  14: form['resposta-14'], 15: form['resposta-15', 16: form['resposta-16']]})
        refresh_view()
        return HttpResponseRedirect("/")


def grafico(request):
    return render(request, 'graph/grafico.html')

def apicurso(request):
    campus = request.GET.get("campus")
    grafico = request.GET.get("grafico")
    cursos = []
    if(int(grafico) == 0 or grafico == None):
        cur.execute('select nome, id from graph_curso where campus_id = {}'.format(campus))
        for i in cur.fetchall():
            cursos.append({'id': i[1], 'nome': i[0]})
        
    if(int(grafico) > 1):
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


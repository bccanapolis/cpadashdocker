import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Campus, Segmento, Curso, Pergunta, ParticipacaoPergunta, Grafico, RespostaObjetiva, CursoCampus, \
    Atuacao, Lotacao, Pessoa
from django.db import connection
import json
from django.http import JsonResponse


def index(request):
    obrigado = request.GET.get('obrigado')
    return render(request, "graph/index.html", {'obrigado': obrigado})


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
        perguntas = [{'id': pergunta['id'], 'titulo': pergunta['titulo'], 'tipo': pergunta['tipo'],
                      'lotacao': pergunta['perguntasegmento__lotacao__titulo']} for pergunta in
                     Pergunta.objects.filter(perguntasegmento__segmento__nome=segmento).order_by("dimensao").order_by(
                         "tipo").values('id', 'titulo', 'tipo', 'dimensao', 'perguntasegmento__lotacao__titulo')]
        resp_objetivas = [{'id': pergunta['id'], 'titulo': pergunta['titulo'], 'value': pergunta['value']} for pergunta
                          in RespostaObjetiva.objects.all().order_by("-value").values('id', 'titulo', 'value')]
        return render(request, "graph/answer.html", {
            "route": segmento, "cursos": cursos, "tiposPessoa": tiposPessoa, "campus": campuses, "perguntas": perguntas,
            "resp_objetivas": resp_objetivas
        })
    elif request.method == "POST":
        form = request.POST
        naoaplica = request.POST.get("naoaplica")
        ParticipacaoPergunta.create_participacao(naoaplica=naoaplica, atuacao=form['atuacao'], lotacao=form['lotacao'],
                                                 segmento=segmento, curso=form['curso'], campus=form['campus'],
                                                 perguntas=form)
        # with connection.cursor() as cursor:
        #     cursor.execute('refresh materialized view informacoes')
        #     cursor.close()
        return HttpResponseRedirect("/?obrigado=true")


def grafico(request):
    pessoas = Pessoa.objects.count()
    return render(request, 'graph/grafico.html', {'total_votacao': pessoas})


def apiatuacao(request):
    pergunta = request.GET.get('pergunta', None)
    campus = request.GET.get("campus", None)
    segmento = request.GET.get("segmento", None)
    atuacao = []
    if pergunta is not None:
        sql = 'select distinct atuacao_id, atuacao from informacoes where pergunta_id = {} '.format(int(pergunta))
        if campus is not None:
            sql += 'and campus_id = {} '.format(int(campus))
        if segmento is not None:
            sql += 'and segmento_id = {} '.format(int(segmento))
        sql += 'and atuacao IS NOT NULL order by atuacao'
        with connection.cursor() as cursor:
            cursor.execute(sql)
            atuacao = [{'id': row[0], 'nome': row[1]} for row in cursor.fetchall()]

    else:
        atuacao = [{'id': atuacao['id'], 'nome': atuacao['titulo']} for atuacao in
                   Atuacao.objects.values('id', 'titulo').all()]
    return JsonResponse({"atuacao": atuacao})


def apilotacao(request):
    pergunta = request.GET.get('pergunta', None)
    campus = request.GET.get("campus", None)
    segmento = request.GET.get("segmento", None)
    lotacao = []
    if pergunta is not None:
        sql = 'select distinct lotacao_id, lotacao from informacoes where pergunta_id = {} '.format(int(pergunta))
        if campus is not None:
            sql += 'and campus_id = {} '.format(int(campus))
        if segmento is not None:
            sql += 'and segmento_id = {} '.format(int(segmento))
        sql += 'and lotacao IS NOT NULL order by lotacao'

        with connection.cursor() as cursor:
            cursor.execute(sql)
            lotacao = [{'id': row[0], 'nome': row[1]} for row in cursor.fetchall()]
    else:
        lotacao = [{'id': lotacao['id'], 'nome': lotacao['titulo']} for lotacao in
                   Lotacao.objects.values('id', 'titulo').all()]
    return JsonResponse({"lotacao": lotacao})


def apicurso(request):
    pergunta = request.GET.get("pergunta", None)
    campus = request.GET.get("campus", None)
    segmento = request.GET.get("segmento", None)
    cursos = []
    if pergunta is None:
        cursos = [{'id': curso['id'], 'nome': curso['nome']} for curso in
                  Curso.objects.filter(cursocampus__campus_id=campus).exclude(nome='Não Aplica').order_by(
                      'nome').values(
                      'nome', 'id')]
    else:
        sql = 'select distinct curso_id, curso from informacoes where curso != \'Não Aplica\' and pergunta_id = {} '.format(
            int(pergunta))
        if campus is not None:
            sql += 'and campus_id = {} '.format(int(campus))
        if segmento is not None:
            sql += 'and segmento_id = {} '.format(int(segmento))
        sql += 'order by curso'

        with connection.cursor() as cursor:
            cursor.execute(sql)
            cursos = [{'id': row[0], 'nome': row[1]} for row in cursor.fetchall()]
    return JsonResponse({"cursos": cursos})


def apicampus(request):
    pergunta = request.GET.get("pergunta")
    segmento = request.GET.get("segmento", None)
    campus = []
    if int(pergunta) == 0 and segmento is None:
        with connection.cursor() as cursor:
            cursor.execute(
                'select distinct campus, campus_id from informacoes order by campus;')
            campus = [{'id': row[1], 'campus': row[0]} for row in cursor.fetchall()]
    elif int(pergunta) == 0:
        with connection.cursor() as cursor:
            cursor.execute(
                'select distinct campus, campus_id from informacoes where segmento_id = {} order by campus;'.format(
                    int(segmento)))
            campus = [{'id': row[1], 'campus': row[0]} for row in cursor.fetchall()]
    elif segmento is None:
        with connection.cursor() as cursor:
            cursor.execute(
                'select distinct campus, campus_id from informacoes where pergunta_id = {} order by campus;'.format(
                    int(pergunta)))
            campus = [{'id': row[1], 'campus': row[0]} for row in cursor.fetchall()]
    else:
        with connection.cursor() as cursor:
            cursor.execute(
                'select distinct campus, campus_id from informacoes where pergunta_id = {} and segmento_id = {} order by campus;'.format(
                    int(pergunta), int(segmento)))
            campus = [{'id': row[1], 'campus': row[0]} for row in cursor.fetchall()]

    return JsonResponse({'campus': campus})


def apigrafico(request):
    update = request.GET.get("update", None)
    pergunta = request.GET.get("pergunta", None)
    segmento = request.GET.get("segmento", None)
    atuacao = request.GET.get("atuacao", None)
    lotacao = request.GET.get("lotacao", None)
    campus = request.GET.get("campus", None)
    curso = request.GET.get("curso", None)
    data = []
    segmentos = []
    respostas = []
    if update is not None:
        with connection.cursor() as cursor:
            cursor.execute('refresh materialized view informacoes')
            cursor.close()
        return HttpResponseRedirect('/QthDtt4r')
    elif pergunta is None:
        with connection.cursor() as cursor:
            cursor.execute(
                'select distinct pergunta_id, pergunta from informacoes where pergunta not like \'Caso%\' order by pergunta')
            data = [{'id': row[0], 'titulo': row[1]} for row in cursor.fetchall()]

        return JsonResponse({'dados': data})
    elif pergunta is not "0":
        sql = 'select count(pessoa), segmento, resposta, resposta_id from informacoes where '
        sql += 'pergunta_id = {} '.format(int(pergunta))
        if segmento is not None:
            sql += ' and segmento_id = {} '.format(int(segmento))
        if campus is not None:
            sql += ' and campus_id = {} '.format(int(campus))
        if curso is not None:
            sql += ' and curso_id = {} '.format(int(curso))
        if atuacao is not None:
            sql += ' and atuacao_id = {} '.format(int(atuacao))
        if lotacao is not None:
            sql += ' and lotacao = {} '.format(int(lotacao))

        sql += ' group by segmento, resposta, resposta_id order by resposta_id'
        total = 0
        indicador = 0
        with connection.cursor() as cursor:
            cursor.execute(sql)
            graficos = cursor.fetchall()
            data = [{'count': row[0], 'segmento': row[1], 'resposta': row[2]} for row in graficos]
            for row in graficos:
                total += row[0]
                if row[1] not in segmentos:
                    segmentos.append(row[1])
                if row[2] not in respostas:
                    respostas.append(row[2])
                if row[2] == 'Ótimo' or row[2] == 'Bom':
                    indicador += row[0]
            total = round((indicador * 100 / total) * 10) / 10
        if total > 75:
            indicador = {'label': 'Manter', 'valor': total, 'cor': '#008ffb'}
        elif total > 50:
            indicador = {'label': 'Desenvolver', 'valor': total, 'cor': '#00e396'}
        elif total > 25:
            indicador = {'label': 'Melhorar', 'valor': total, 'cor': '#feb019'}
        else:
            indicador = {'label': 'Sanar', 'valor': total, 'cor': '#ff4560'}
        pergunta = Pergunta.objects.get(pk=pergunta).titulo
        return JsonResponse(
            {'pergunta': pergunta, 'indicador': indicador, 'roles': segmentos, 'respostas': respostas,
             'data': data})
    else:
        sql = 'select count(distinct pessoa), campus'
        fetch = ''
        group = ' group by campus'
        where = ''

        if campus is not None and segmento is not None:
            nome_segmento = Segmento.objects.get(pk=segmento).nome
            fetch = ', segmento'
            group += ', segmento'
            where += ' where segmento_id = {} and campus_id = {} '.format(int(segmento), int(campus))
            print(nome_segmento)
            if nome_segmento == "Docente":
                fetch += ', atuacao '
                group += ', atuacao '
            elif nome_segmento == "Estudante":
                fetch += ', curso '
                group += ', curso '
            elif nome_segmento == 'Técnico Administrativo Campus' or nome_segmento == 'Técnico Administrativo Reitoria':
                fetch += ', lotacao '
                group += ', lotacao '
        elif segmento is not None:
            fetch = ', segmento'
            group += ', segmento'
            where += ' where segmento_id = {}'.format(int(segmento))
        elif campus is not None:
            fetch = ', segmento'
            group += ', segmento'
            where += ' where campus_id = {}'.format(int(campus))

        sql = sql + fetch + ' from informacoes ' + where + group
        with connection.cursor() as cursor:
            cursor.execute(sql)
            graficos = cursor.fetchall()
        for row in graficos:
            if campus is not None and segmento is not None:
                data.append({'count': row[0], 'label': row[3]})
                segmentos.append(row[3])
            elif campus is not None:
                data.append({'count': row[0], 'label': row[2]})
                segmentos.append(row[2])
            else:
                data.append({'count': row[0], 'label': row[1]})
                segmentos.append(row[1])

        return JsonResponse({'roles': segmentos, 'data': data})


def apisegmento(request):
    pergunta = request.GET.get('pergunta', None)
    segmentos = []
    if pergunta is not None:
        with connection.cursor() as cursor:
            cursor.execute(
                'select distinct segmento_id, segmento from informacoes where pergunta_id = {} order by segmento'.format(
                    pergunta))
            segmentos = [{'id': row[0], 'nome': row[1]} for row in cursor.fetchall()]
    return JsonResponse({'segmentos': segmentos})

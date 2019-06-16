from django.db import connection, transaction
from collections import defaultdict
import operator

@transaction.atomic
# request materialized views
def fetch_view(view, campus, curso):
    campus = campus if campus != '0' and campus != None else 'campus_id'
    curso = curso if curso != '0' and curso != None else 'curso_id'
    with connection.cursor() as cursor:
        cursor.execute(
            'select count(resposta), resposta, segmento from public.graph_view{} where campus_id = {} and curso_id = {} group by resposta, segmento order by segmento;'.format(view, campus, curso))
        row = cursor.fetchall()
    print(row)
    return row


def fetch_view1(campus):
    print(campus)
    with connection.cursor() as cursor:
        if campus == "0" or campus == None:
            cursor.execute(
            'select sum(quant) as quant, campus from public.graph_view1 group by campus having sum(quant) > 0 order by campus ;')
            row = cursor.fetchall()
        else:
            cursor.execute('select sum(quant) as quant, campus, curso from public.graph_view1 where campus_id = {} group by campus, curso having sum(quant) > 0 order by campus;'.format(campus))
            row = cursor.fetchall()
    return row


@transaction.atomic
def refresh_view():
    with connection.cursor() as cursor:
        cursor.execute('refresh materialized view graph_view1')
        #cursor.execute('refresh materialized view graph_view2')
        cursor.execute('refresh materialized view graph_view3')
        cursor.execute('refresh materialized view graph_view4')
        cursor.execute('refresh materialized view graph_view5')
        cursor.execute('refresh materialized view graph_view6')
        cursor.execute('refresh materialized view graph_view7')
        cursor.execute('refresh materialized view graph_view8')
        #cursor.execute('refresh materialized view graph_view9')
        cursor.execute('refresh materialized view graph_view10')
        cursor.execute('refresh materialized view graph_view11')
        cursor.execute('refresh materialized view graph_view12')
        cursor.execute('refresh materialized view graph_view13')
        cursor.execute('refresh materialized view graph_view14')
        cursor.execute('refresh materialized view graph_view15')
        cursor.execute('refresh materialized view graph_view16')
        cursor.execute('refresh materialized view graph_view17')
        cursor.execute('refresh materialized view graph_view18')
        cursor.execute('refresh materialized view graph_view19')
        cursor.execute('refresh materialized view graph_view20')

def query_view(view):
    if(view != 1):
        campuses = []
        cursos = {}
        segmentos = []
        with connection.cursor() as cursor:
            cursor.execute(
                "select campus, campus_id, curso, curso_id from public.graph_view%s group by campus, campus_id, curso, curso_id order by curso", [view])
            value = cursor.fetchall()
            for item in value:
                campus = {item[1]: item[0]}
                if campus not in campuses:
                    campuses.append(campus)
                    cursos[item[0]] = []
                curso = {item[3]: item[2]}
                if curso not in cursos[item[0]]:
                    cursos[item[0]].append(curso)

            cursor.execute(
                "select segmento_id, segmento from public.graph_view%s group by segmento_id, segmento order by segmento", [view])
            value = cursor.fetchall()
            for item in value:
                segmento = {item[0]: item[1]}
                if segmento not in segmentos:
                    segmentos.append(segmento)
    
        return {'idpage': view, 'campus': campuses, 'cursos': cursos , 'segmentos': segmentos}

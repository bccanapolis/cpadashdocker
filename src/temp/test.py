import xlrd
import psycopg2 as psy
from collections import defaultdict

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

file2 = xlrd.open_workbook('alunocurso.xlsx')
sheet2 = file2.sheet_by_index(0) 
file1 = xlrd.open_workbook('cpadash_data.xls')
sheet = file1.sheet_by_index(0)
def addAlunoCurso():
    cont = 1
    for i in range(1, sheet2.nrows):
        hca = sheet2.cell_value(i, 0)
        hcu = sheet2.cell_value(i, 1)
        hqt = sheet2.cell_value(i, 2)
        cur.execute("select id from graph_campus where nome = %s", [hca])
        idca = cur.fetchone()[0]
        cur.execute("select cu.nome, cu.id, cu.campus_id, ca.nome from graph_curso cu left join graph_campus ca on cu.campus_id = ca.id where cu.nome = %s and ca.nome = %s", [hcu, hca])
        res = cur.fetchone()
        if res is None:
            cur.execute("insert into graph_curso (id, nome, quant, campus_id) values (DEFAULT, %s, %s, %s)", [hcu, hqt, idca])
        else:
            cur.execute("update graph_curso set quant = %s where id = %s and campus_id = %s;", [hqt, res[1], idca])
        con.commit()
        print("inserido", cont)
        cont += 1


def addGrafico():
    string = 'insert into public."graph_grafico" (id, numero, pergunta_id,titulo) values '
    string += "(DEFAULT, 1, NULL, 'Quantidade e Proporção de Discentes por Câmpus'), "
    string += "(DEFAULT, 3, 1, 'Você conhece os resultados do último processo de autoavaliação institucional realizado pela Comissão Própria de Avaliação (CPA)?' ), "    
    string += "(DEFAULT, 4, 3, 'Você participou do Planejamento do ano de 2018 na Pró-Reitoria a qual você está vinculado(a)?'), "
    string += "(DEFAULT, 5, 5, 'Você participa da elaboração do Planejamento anual do seu Câmpus?'), "
    string += "(DEFAULT, 6, 4, 'Você considera satisfatória a divulgação do Planejamento anual do seu Câmpus?'), "
    string += "(DEFAULT, 7, 6, 'Os cursos ofertados no seu Câmpus atendem as demandas socioeconômicas da região ? '), "
    string += "(DEFAULT, 8, 7, 'De maneira geral, você considera que a formação que está recebendo é de boa qualidade? '), "
    string += "(DEFAULT, 10, 8, 'Você acompanha os trabalhos do Conselho de Ensino Pesquisa e Extensão (CONEPEX)?'), "
    string += "(DEFAULT, 11, 9, 'Você conhece ou participa de algum Projeto de Pesquisa do IFG?'), "
    string += "(DEFAULT, 12, 9, 'Você conhece ou participa de algum Projeto de Pesquisa do IFG?'), "
    string += "(DEFAULT, 13, 10, 'Você conhece ou participa de algum Projeto de Extensão do IFG?'), "
    string += "(DEFAULT, 14, 16, 'Você conhece ou participa de algum Projeto de Ensino?'), "
    string += "(DEFAULT, 15, 16, 'Você conhece ou participa de algum Projeto de Ensino?'), "
    string += "(DEFAULT, 16, 13, 'Você considera satisfatória a atuação do IFG para promoção da permanência e êxito dos/das estudantes?'), "
    string += "(DEFAULT, 17, 11, 'Você considera satisfatória a comunicação do IFG por meio do site e das redes sociais?'), "
    string += "(DEFAULT, 18, 14, 'Proporção de respostas positivas e negativas no que diz respeito ao conhecimento da função da Ouvidoria pela comunidade acadêmica.'), "
    string += "(DEFAULT, 19, 14, 'Você conhece a função da ouvidoria do IFG?'), "
    string += "(DEFAULT, 20, 12, 'De maneira geral, você é bem atendido/a nos setores de atendimento ao/à discente/docente no IFG?')"
    print(string)
    cur.execute(string)
    con.commit()

def addCampus():
    unique_list = []
    for i in range(1, sheet.nrows):
        x = sheet.cell_value(i, 7)
        if x not in unique_list:
            unique_list.append(x)

    for i in range(0, len(unique_list)):
        string = 'insert into graph_campus (id, nome) values (DEFAULT, \'{}\') returning id'.format(unique_list[i])
        cur.execute(string)
        idCurso = cur.fetchone()[0]
        cur.execute("insert into graph_curso (id, nome, campus_id) values (DEFAULT, 'Não Informado', %s)", [idCurso])
        con.commit()
        print("Inserido campus", str(unique_list[i]))


def addCursos():
    cursos = getCursosCampus()
    for x, v in cursos.items():
        cur.execute('select id from graph_campus where nome = \'{}\''.format(x))
        cursorid = cur.fetchone()
        for y in v:
            cur.execute('insert into graph_curso (id, nome, campus_id) values (DEFAULT ,\'{}\', {})'.format(y, cursorid[0]))
            con.commit()
            print("Inserido curso", y)
    con.commit()

def addSegmentos():
    # adiciona segmentos de pessoas
    cur.execute("insert into graph_segmento (id, nome) values (DEFAULT, 'Docente'), (DEFAULT, 'Estudante'), (DEFAULT, 'Técnico-Administrativo')")
    con.commit()
    print("Inserido segmentos: Estudante, Docente e Técnico-Administrativo")


def sanitizeCurso(linha):
    cels = []
    curso = ''
    for y in range(8, 19):
        cels.append(sheet.cell_value(linha, y))
    for y in range(0, len(cels)):
        if cels[y] != '':
            curso = cels[y]
    return curso

def getCursosCampus():
    cursos = defaultdict(list)
    for x in range(1, sheet.nrows):
        values = []
        value = ''
        curso = sheet.cell_value(x, 7)
        for y in range(8, 19):
            values.append(sheet.cell_value(x, y))
        for y in range(0, len(values)):
            if values[y] != '':
                value = values[y]
        if value != '' and value not in cursos[curso]:
            cursos[curso].append(value)
    return cursos


def addPerguntas():
    # adiciona perguntas ao banco
    for x in range(20, 36):
        string = 'insert into graph_pergunta (id, titulo) values (DEFAULT,\'{}\')'.format(sheet.cell_value(0, x).replace('\xa0', ''))
        cur.execute(string)
        con.commit()

def addPessoa(segmento):
    cur.execute("INSERT INTO graph_pessoa (id, nome, segmento_id) values (DEFAULT, '', %s) RETURNING id", [segmento])
    idPessoa = cur.fetchone()[0]
    con.commit()
    return idPessoa

def addPessoaCurso(linha, campus, pessoa):
    idCurso = 0
    if (sanitizeCurso(linha) != ''):
        cur.execute('select id, nome from graph_curso where campus_id = {} and nome = \'{}\''.format(campus, sanitizeCurso(linha)))
        idCurso = cur.fetchone()[0]
        cur.execute("insert into graph_pessoacurso (id, curso_id, pessoa_id) values (DEFAULT, %s,%s)", [idCurso, pessoa])
        con.commit()

    else:
        cur.execute('select id, nome from graph_curso where campus_id = {} and nome = \'Não Informado\''.format(campus))
        idCursoNulo = cur.fetchone()[0]
        cur.execute("insert into graph_pessoacurso (id, curso_id, pessoa_id) values (DEFAULT, %s,%s)", [idCursoNulo, pessoa])
        con.commit()
    
    return idCurso


def addParticipacaoPergunta(pergunta, resposta, pessoa):
    cur.execute("INSERT INTO graph_participacaopergunta (id, resposta, pergunta_id, pessoa_id) values (DEFAULT, %s, %s, %s) RETURNING id", [resposta, pergunta, pessoa])
    idParticipacao = cur.fetchone()[0]

    return (idParticipacao is not None)


#add participacao
def addParticipacao():
    cur.execute("select * from graph_segmento")
    holdSeg = cur.fetchall()
    segmentos = {holdSeg[0][1]: holdSeg[0][0], holdSeg[1][1]: holdSeg[1][0], holdSeg[2][1]: holdSeg[2][0]}
    cur.execute("select * from graph_campus")
    campuses = {}
    for i in cur.fetchall():
        campuses[i[1]] = i[0]
        
    for linha in range(1, sheet.nrows):
        segmento = sheet.cell_value(linha, 6)
        campus = sheet.cell_value(linha, 7)
        
        idPessoa = addPessoa(segmentos[segmento])
        idCurso = addPessoaCurso(linha, campuses[campus], idPessoa)


        respostas = {}
        for i in range(1,17):
            value = sheet.cell_value(linha, i+19)
            respostas[i] = value

        for x in range(1,len(respostas)+1):
            addParticipacaoPergunta(x, respostas[x], idPessoa)
    cur.execute("update graph_participacaopergunta set resposta = 'Não' where resposta = 'nao'")
    cur.execute("update graph_participacaopergunta set resposta = 'Sim' where resposta = 'sim'")
    cur.execute("update graph_segmento set nome = 'Discente' where nome = 'Estudante'");
    con.commit()
        
addSegmentos()
addCampus()
addAlunoCurso()
addCursos()
addPerguntas()
addGrafico()



addParticipacao()
con.close()

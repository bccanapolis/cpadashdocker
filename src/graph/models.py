from datetime import datetime

from django.db import models
from django.utils import timezone

#TODO Arrumar para escalar perguntas por ano: todos os será adicionado novas perguntas e/ou utilizadas as já no banco de dados, portanto é necessário adicionar uma data para cara pergunta/segmento

class Segmento(models.Model):
    class Meta:
        verbose_name_plural = 'Segmento'

    nome = models.CharField(max_length=64)

    def __str__(self):
        return self.nome


class Atuacao(models.Model):
    class Meta:
        verbose_name_plural = 'Atuacao'

    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Lotacao(models.Model):
    class Meta:
        verbose_name_plural = 'Lotacoes'

    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Campus(models.Model):
    class Meta:
        verbose_name_plural = 'Campus'

    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    class Meta:
        verbose_name_plural = 'Curso'

    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Eixo(models.Model):
    class Meta:
        verbose_name_plural = 'Eixo'

    eixo = models.CharField(max_length=100)

    def __str__(self):
        return self.eixo


class Dimensao(models.Model):
    class Meta:
        verbose_name_plural = 'Dimensao'

    dimensao = models.CharField(max_length=100)
    eixo = models.ForeignKey(Eixo, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.dimensao


class CursoCampus(models.Model):
    class Meta:
        verbose_name_plural = 'CursoCampus'

    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    quant = models.IntegerField(null=True)

    def __str__(self):
        return "{} -- {}".format(self.campus, self.curso)


class Pessoa(models.Model):
    class Meta:
        verbose_name_plural = 'Pessoa'

    segmento = models.ForeignKey(
        Segmento, null=True, on_delete=models.SET_NULL)
    atuacao = models.ForeignKey(Atuacao, null=True, on_delete=models.SET_NULL)
    lotacao = models.ForeignKey(Lotacao, null=True, on_delete=models.SET_NULL)
    curso = models.ForeignKey(CursoCampus, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    class Meta:
        verbose_name_plural = 'Pergunta'

    titulo = models.TextField()
    tipo = models.IntegerField(null=False, default=1)

    dimensao = models.ForeignKey(Dimensao, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo


class PerguntaSegmento(models.Model):
    class Meta:
        verbose_name_plural = 'PerguntaSegmento'

    YEAR_CHOICES = []
    for r in range(2019, datetime.now().year + 1):
        YEAR_CHOICES.append((r,r))

    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    atuacao = models.ForeignKey(Atuacao, null=True, on_delete=models.SET_NULL)
    lotacao = models.ForeignKey(Lotacao, null=True, on_delete=models.SET_NULL)
    ano = models.IntegerField(default=datetime.now().year, choices=YEAR_CHOICES)

    def __str__(self):
        return "{} -- {} -- {}".format(self.ano, self.segmento, self.pergunta)


class Grafico(models.Model):
    class Meta:
        verbose_name_plural: "Grafico"

    titulo = models.TextField()
    numero = models.IntegerField(null=True)
    pergunta = models.ForeignKey(
        Pergunta, blank=True, null=True, on_delete=models.SET_NULL)
    topico = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo


class RespostaObjetiva(models.Model):
    class Meta:
        verbose_name_plural: "RespostaObjetiva"

    titulo = models.CharField(max_length=24)
    value = models.IntegerField(null=False, default=1)

    def __str__(self):
        return self.titulo


class ParticipacaoPergunta(models.Model):
    class Meta:
        verbose_name_plural = 'ParticipacaoPergunta'

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    res_subjetiva = models.TextField(null=True)
    res_objetiva = models.ForeignKey(RespostaObjetiva, null=True, on_delete=models.SET_NULL)
    ano = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return "{} {}".format(self.pessoa, self.pergunta)

    def create_participacao(atuacao, lotacao, segmento, curso, campus, perguntas):
        pessoaId = None
        segmento = Segmento.objects.get(pk=int(segmento)).nome
        if segmento == "Técnico Administrativo Câmpus":
            pessoaId = Pessoa.objects.create(segmento=Segmento.objects.get(nome=segmento),
                                             atuacao=None,
                                             lotacao=Lotacao.objects.get(id=int(lotacao)),
                                             curso=CursoCampus.objects.get(campus_id=int(campus),
                                                                           curso__nome='Não Aplica')
                                             )
        elif segmento == "Técnico Administrativo Reitoria":
            pessoaId = Pessoa.objects.create(segmento=Segmento.objects.get(nome=segmento),
                                  atuacao=None,
                                  lotacao=None,
                                  curso=CursoCampus.objects.get(campus_id=int(campus),
                                                                curso__nome='Não Aplica')
                                  )

        elif segmento == "Docente":
            pessoaId = Pessoa.objects.create(segmento=Segmento.objects.get(nome=segmento),
                                  atuacao=Atuacao.objects.get(id=int(atuacao)),
                                  lotacao=None,
                                  curso=CursoCampus.objects.get(campus_id=int(campus),
                                                                curso__nome='Não Aplica')
                                  )
        elif segmento == 'Estudante':
            pessoaId = Pessoa.objects.create(segmento=Segmento.objects.get(nome=segmento),
                                             atuacao=None,
                                             lotacao=None,
                                             curso=CursoCampus.objects.get(campus_id=int(campus),
                                                                           curso_id=int(curso))
                                             )
        print(type(perguntas))
        for key, value in perguntas.items():
                pergunta = Pergunta.objects.get(pk=key)

                if pergunta.tipo == 1:
                    ParticipacaoPergunta.objects.create(pessoa=pessoaId, pergunta=Pergunta.objects.get(pk=key),
                                                        res_objetiva=RespostaObjetiva.objects.get(pk=value), ano=timezone.now())
                else:
                    ParticipacaoPergunta.objects.create(pessoa=pessoaId, pergunta=Pergunta.objects.get(pk=key),
                                                        res_subjetiva=value, ano=timezone.now())

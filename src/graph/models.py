from django.db import models


# Create your models here.


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
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo


class Pessoa(models.Model):
    class Meta:
        verbose_name_plural = 'Pessoa'

    segmento = models.ForeignKey(
        Segmento, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


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

    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)

    def __str__(self):
        return "{} -- {}".format(self.segmento, self.pergunta)


class CursoCampus(models.Model):
    class Meta:
        verbose_name_plural = 'CursoCampus'

    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    quant = models.IntegerField(null=True)

    def __str__(self):
        return "{} {}".format(self.campus, self.curso)


class PessoaCurso(models.Model):
    class Meta:
        verbose_name_plural = 'PessoaCurso'

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(CursoCampus, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.pessoa, self.curso)


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

    def __str__(self):
        return "{} {}".format(self.pessoa, self.pergunta)

    def create_participacao(segmento, curso, campus, perguntas):
        pessoaId = Pessoa.objects.create(segmento=Segmento.objects.get(nome=segmento))
        pessoaCurso = PessoaCurso.objects.create(pessoa=pessoaId, curso=CursoCampus.objects.get(campus_id=campus, curso_id=curso))

        for key, value in perguntas.dict().items():
            if key.startswith('resposta-') and value != "":
                perguntaKey = int(key.replace("resposta-", ""))
                pergunta = Pergunta.objects.get(pk= perguntaKey)
                if pergunta.tipo == 1:
                    ParticipacaoPergunta.objects.create(pessoa=pessoaId, pergunta=Pergunta.objects.get(pk=perguntaKey), res_objetiva=RespostaObjetiva.objects.get(pk=value))
                else:
                    ParticipacaoPergunta.objects.create(pessoa=pessoaId, pergunta=Pergunta.objects.get(pk=perguntaKey),
                                                        res_subjetiva=value)
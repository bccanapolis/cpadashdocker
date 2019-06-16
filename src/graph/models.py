from django.db import models

# Create your models here.


class Segmento(models.Model):
    class Meta:
        verbose_name_plural = 'Segmento'

    nome = models.CharField(max_length=32)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    class Meta:
        verbose_name_plural = 'Pessoa'

    nome = models.CharField(max_length=70)
    segmento = models.ForeignKey(
        Segmento, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


class Campus(models.Model):
    class Meta:
        verbose_name_plural = 'Campus'

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Curso(models.Model):
    class Meta:
        verbose_name_plural = 'Curso'

    nome = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, null=True, on_delete=models.SET_NULL)
    quant = models.IntegerField(null=True)

    def __str__(self):
        return self.nome


class Tema(models.Model):
    class Meta:
        verbose_name_plural = 'Tema'

    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Pergunta(models.Model):
    class Meta:
        verbose_name_plural = 'Pergunta'

    titulo = models.TextField()
    tema = models.ForeignKey(Tema, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo


class PessoaCurso(models.Model):
    class Meta:
        verbose_name_plural = 'PessoaCurso'

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)

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


class ParticipacaoPergunta(models.Model):
    class Meta:
        verbose_name_plural = 'ParticipacaoPergunta'

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.TextField()

    def __str__(self):
        return "{} {}".format(self.pessoa, self.pergunta)

    def create_participacao(pessoa, segmento, curso, perguntas):
        pessoaId = Pessoa.objects.create(
            nome=pessoa, segmento=Segmento.objects.get(pk=segmento))
        # pessoaCurso = PessoaCurso.objects.create(pessoa=pessoaId, curso=Curso.objects.get(pk=curso))

        for key in perguntas:
            ParticipacaoPergunta.objects.create(
                pessoa=pessoaId, pergunta=Pergunta.objects.get(pk=key), resposta=perguntas[key])

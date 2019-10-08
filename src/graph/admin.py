from django.contrib import admin
from .models import Pessoa, Curso, Campus, Eixo, Pergunta, Segmento, Grafico, Atuacao, Dimensao, PessoaCurso, ParticipacaoPergunta, CursoCampus, PerguntaSegmento, RespostaObjetiva

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Curso)
admin.site.register(Campus)
admin.site.register(Eixo)
admin.site.register(Pergunta)
admin.site.register(Segmento)
admin.site.register(Grafico)
admin.site.register(Atuacao)
admin.site.register(Dimensao)
admin.site.register(PessoaCurso)
admin.site.register(ParticipacaoPergunta)
admin.site.register(CursoCampus)
admin.site.register(PerguntaSegmento)
admin.site.register(RespostaObjetiva)
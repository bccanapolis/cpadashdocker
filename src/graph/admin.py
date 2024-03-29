from django.contrib import admin
from .models import Pessoa, Curso, Campus, Eixo, Pergunta, Segmento, Atuacao, Dimensao, ParticipacaoPergunta, \
    CursoCampus, PerguntaSegmento, RespostaObjetiva, Lotacao, Questionario

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Curso)
admin.site.register(Campus)
admin.site.register(Eixo)
admin.site.register(Pergunta)
admin.site.register(Segmento)
admin.site.register(Lotacao)
admin.site.register(Atuacao)
admin.site.register(Dimensao)
admin.site.register(ParticipacaoPergunta)
admin.site.register(CursoCampus)
admin.site.register(PerguntaSegmento)
admin.site.register(RespostaObjetiva)
admin.site.register(Questionario)
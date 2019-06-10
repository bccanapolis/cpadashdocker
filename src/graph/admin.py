from django.contrib import admin
from .models import Pessoa, Curso, Campus, Tema, Pergunta, Segmento, Grafico

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Curso)
admin.site.register(Campus)
admin.site.register(Tema)
admin.site.register(Pergunta)
admin.site.register(Segmento)
admin.site.register(Grafico)
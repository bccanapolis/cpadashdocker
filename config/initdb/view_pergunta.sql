select pergunta.titulo as pergunta,
       pessoacurso.pessoa_id,
       segmento.nome as segmento,
       objetiva.titulo as resposta,
       curso.nome as curso,
       campus.nome as campus,
       atuacao.titulo as atuacao,
       lotacao.titulo as lotacao
from graph_participacaopergunta participacao
left join graph_pergunta pergunta on participacao.pergunta_id = pergunta.id
left join graph_pessoa pessoa on participacao.pessoa_id = pessoa.id
left join graph_pessoacurso pessoacurso on pessoa.id = pessoacurso.pessoa_id
left join graph_atuacao atuacao on pessoa.atuacao_id = atuacao.id
left join graph_respostaobjetiva objetiva on participacao.res_objetiva_id = objetiva.id
left join graph_lotacao lotacao on pessoa.lotacao_id = lotacao.id
left join graph_cursocampus gc on pessoacurso.curso_id = gc.id
left join graph_campus campus on gc.campus_id = campus.id
left join graph_curso curso on gc.curso_id = curso.id
left join graph_segmento segmento on pessoa.segmento_id = segmento.id

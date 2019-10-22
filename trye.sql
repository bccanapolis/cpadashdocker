select resp.titulo            as resposta,
       count(res_objetiva_id) as count,
       campus.nome            as campus
from graph_participacaopergunta as part
         left join graph_respostaobjetiva as resp on part.res_objetiva_id = resp.id
         left join graph_pergunta pergunta on part.pergunta_id = pergunta.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         left join graph_pessoacurso pessoacurso on pessoa.id = pessoacurso.pessoa_id
         left join graph_cursocampus cursocampus on pessoacurso.curso_id = cursocampus.id
         left join graph_curso curso on cursocampus.curso_id = curso.id
         left join graph_campus campus on cursocampus.campus_id = campus.id
         left join graph_atuacao atuacao on pessoa.atuacao_id = atuacao.id
         left join graph_lotacao lotacao on pessoa.lotacao_id = lotacao.id
where pergunta.id = 1 and pergunta.tipo = 1
group by resp.titulo, campus.nome;


SELECT "graph_participacaopergunta"."pessoa_id",
       T4."res_objetiva_id",
       "graph_segmento"."nome",
       "graph_pessoa"."segmento_id",
       "graph_curso"."nome",
       T10."titulo",
       "graph_atuacao"."titulo",
       "graph_lotacao"."titulo",
       COUNT(T4."res_objetiva_id") AS "count"
FROM "graph_participacaopergunta"
         INNER JOIN "graph_pergunta" ON ("graph_participacaopergunta"."pergunta_id" = "graph_pergunta"."id")
         INNER JOIN "graph_pessoa" ON ("graph_participacaopergunta"."pessoa_id" = "graph_pessoa"."id")
         LEFT OUTER JOIN "graph_participacaopergunta" T4 ON ("graph_pergunta"."id" = T4."pergunta_id")
         LEFT OUTER JOIN "graph_segmento" ON ("graph_pessoa"."segmento_id" = "graph_segmento"."id")
         LEFT OUTER JOIN "graph_pessoacurso" ON ("graph_pessoa"."id" = "graph_pessoacurso"."pessoa_id")
         LEFT OUTER JOIN "graph_cursocampus" ON ("graph_pessoacurso"."curso_id" = "graph_cursocampus"."id")
         LEFT OUTER JOIN "graph_curso" ON ("graph_cursocampus"."curso_id" = "graph_curso"."id")
         LEFT OUTER JOIN "graph_respostaobjetiva" T10 ON ("graph_participacaopergunta"."res_objetiva_id" = T10."id")
         LEFT OUTER JOIN "graph_atuacao" ON ("graph_pessoa"."atuacao_id" = "graph_atuacao"."id")
         LEFT OUTER JOIN "graph_lotacao" ON ("graph_pessoa"."lotacao_id" = "graph_lotacao"."id")
WHERE ("graph_pergunta"."tipo" = 1 AND "graph_participacaopergunta"."pergunta_id" = 5)
GROUP BY "graph_participacaopergunta"."pessoa_id", T4."res_objetiva_id", "graph_segmento"."nome",
         "graph_pessoa"."segmento_id", "graph_curso"."nome", T10."titulo", "graph_atuacao"."titulo",
         "graph_lotacao"."titulo"
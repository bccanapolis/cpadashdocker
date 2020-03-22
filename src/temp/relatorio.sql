CREATE extension tablefunc;

select *
from crosstab($$
    select pessoa.id as pessoa, segmento.nome as segmento, campus.nome as campus, curso.nome as curso, lotacao.titulo as lotacao, atuacao.titulo as atuacao, res_subjetiva as subjetiva, pergunta.id as pergunta,  objetiva.titulo as objetiva
         from graph_participacaopergunta
         left join graph_pergunta pergunta on graph_participacaopergunta.pergunta_id = pergunta.id
         left join graph_pessoa pessoa on graph_participacaopergunta.pessoa_id = pessoa.id
         left join graph_cursocampus gc on pessoa.curso_id = gc.id
         left join graph_atuacao atuacao on pessoa.atuacao_id = atuacao.id
         left join graph_segmento segmento on pessoa.segmento_id = segmento.id
         left join graph_campus campus on gc.campus_id = campus.id
         left join graph_curso curso on gc.curso_id = curso.id
         left join graph_respostaobjetiva objetiva on graph_participacaopergunta.res_objetiva_id = objetiva.id
         left join graph_lotacao lotacao on pessoa.lotacao_id = lotacao.id
where campus.nome = 'Anápolis'
     $$,
              $$
        SELECT generate_series(1, 28) -- should be (1, 31)
    $$
         ) as final_result(pessoa integer, segmento text, campus text, curso text, lotacao text, atuacao text, subjetiva text, "1" text, "2" text, "3" text, "4" text, "5" text,
                           "6" text, "7" text,
                           "8" text, "9" text, "10" text, "11" text, "12" text, "13" text, "14" text, "15" text,
                           "16" text, "17" text, "18" text, "19" text, "20" text, "21" text, "22" text, "23" text,
                           "24" text,
                           "25" text, "26" text, "27" text, "28" text);

select pessoa.id       as pessoa,
       pergunta.id     as pergunta,
       objetiva.titulo as objetiva,
       lotacao.titulo as lotacao,
       segmento.nome as segmento,
       atuacao.titulo as atuacao,
       campus.nome     as campus,
       curso.nome      as curso,
       res_subjetiva as subjetiva
from graph_participacaopergunta
         left join graph_pergunta pergunta on graph_participacaopergunta.pergunta_id = pergunta.id
         left join graph_pessoa pessoa on graph_participacaopergunta.pessoa_id = pessoa.id
         left join graph_cursocampus gc on pessoa.curso_id = gc.id
         left join graph_atuacao atuacao on pessoa.atuacao_id = atuacao.id
        left join graph_segmento segmento on pessoa.segmento_id = segmento.id
         left join graph_campus campus on gc.campus_id = campus.id
         left join graph_curso curso on gc.curso_id = curso.id
         left join graph_respostaobjetiva objetiva on graph_participacaopergunta.res_objetiva_id = objetiva.id
         left join graph_lotacao lotacao on pessoa.lotacao_id = lotacao.id
where campus.nome = 'Anápolis' and segmento.nome != 'Técnico Administrativo Reitoria'

create materialized view informacoes as
SELECT pergunta.titulo AS pergunta,
       pergunta.id     AS pergunta_id,
       pessoa.id       AS pessoa,
       segmento.nome   AS segmento,
       segmento.id     AS segmento_id,
       objetiva.titulo AS resposta,
       objetiva.id     AS resposta_id,
       curso.id        AS curso_id,
       curso.nome      AS curso,
       campus.nome     AS campus,
       campus.id       AS campus_id,
       atuacao.titulo  AS atuacao,
       atuacao.id      AS atuacao_id,
       lotacao.titulo  AS lotacao,
       lotacao.id      AS lotacao_id,
       extract(year from time) AS ano
FROM graph_participacaopergunta participacao
         LEFT JOIN graph_pergunta pergunta ON participacao.pergunta_id = pergunta.id
         LEFT JOIN graph_pessoa pessoa ON participacao.pessoa_id = pessoa.id
         LEFT JOIN graph_atuacao atuacao ON pessoa.atuacao_id = atuacao.id
         LEFT JOIN graph_respostaobjetiva objetiva ON participacao.res_objetiva_id = objetiva.id
         LEFT JOIN graph_lotacao lotacao ON pessoa.lotacao_id = lotacao.id
         LEFT JOIN graph_cursocampus gc ON pessoa.curso_id = gc.id
         LEFT JOIN graph_campus campus ON gc.campus_id = campus.id
         LEFT JOIN graph_curso curso ON gc.curso_id = curso.id
         LEFT JOIN graph_segmento segmento ON pessoa.segmento_id = segmento.id;
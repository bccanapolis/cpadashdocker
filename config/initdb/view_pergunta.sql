select count(pessoa), segmento, resposta from
       informacoes as pppaolgccs
where pergunta_id = 1
group by segmento, resposta

select distinct pergunta, pergunta_id from informacoes;


select distinct curso_id, curso from informacoes where pergunta_id = 1 and campus_id = 2 order by curso

refresh materialized view informacoes


select count(pessoa), segmento, resposta, resposta_id from informacoes where pergunta_id = 1 and campus_id = 5 and segmento_id = 4 and campus_id = 4 and lotacao_id = 3 group by segmento, resposta, resposta_id order by resposta_id

-- create materialized view informacoes as
-- select pergunta.titulo as pergunta,
--        pergunta.id     as pergunta_id,
--        pessoa.id       as pessoa,
--        segmento.nome   as segmento,
--        segmento.id     as segmento_id,
--        objetiva.titulo as resposta,
--        objetiva.id     as resposta_id,
--        curso.id        as curso_id,
--        curso.nome      as curso,
--        campus.nome     as campus,
--        campus.id       as campus_id,
--        atuacao.titulo  as atuacao,
--        atuacao.id      as atuacao_id,
--        lotacao.titulo  as lotacao,
--        lotacao.id      as lotacao_id
-- from graph_participacaopergunta participacao
--          left join graph_pergunta pergunta on participacao.pergunta_id = pergunta.id
--          left join graph_pessoa pessoa on participacao.pessoa_id = pessoa.id
--          left join graph_atuacao atuacao on pessoa.atuacao_id = atuacao.id
--          left join graph_respostaobjetiva objetiva on participacao.res_objetiva_id = objetiva.id
--          left join graph_lotacao lotacao on pessoa.lotacao_id = lotacao.id
--          left join graph_cursocampus gc on pessoa.curso_id = gc.id
--          left join graph_campus campus on gc.campus_id = campus.id
--          left join graph_curso curso on gc.curso_id = curso.id
--          left join graph_segmento segmento on pessoa.segmento_id = segmento.id
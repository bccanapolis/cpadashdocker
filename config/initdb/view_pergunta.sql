create materialized view informacoes as
select distinct pergunta.titulo   as pergunta,
                participacao.ano  as ano,
                pergunta.id       as pergunta_id,
                eixo.id           as eixo_id,
                eixo.eixo         as eixo,
                dimensao.id       as dimensao_id,
                dimensao.dimensao as dimensao,
                pessoa.id         as pessoa,
                segmento.nome     as segmento,
                segmento.id       as segmento_id,
                objetiva.titulo   as resposta,
                objetiva.id       as resposta_id,
                participacao.res_subjetiva as subjetiva,
                curso.id          as curso_id,
                curso.nome        as curso,
                campus.nome       as campus,
                campus.id         as campus_id,
                atuacao.titulo    as atuacao,
                atuacao.id        as atuacao_id,
                lotacao.titulo    as lotacao,
                lotacao.id        as lotacao_id
from graph_participacaopergunta participacao
         left join graph_pergunta pergunta on participacao.pergunta_id = pergunta.id
         left join graph_pessoa pessoa on participacao.pessoa_id = pessoa.id
         left join graph_atuacao atuacao on pessoa.atuacao_id = atuacao.id
         left join graph_respostaobjetiva objetiva on participacao.res_objetiva_id = objetiva.id
         left join graph_lotacao lotacao on pessoa.lotacao_id = lotacao.id
         left join graph_cursocampus gc on pessoa.curso_id = gc.id
         left join graph_campus campus on gc.campus_id = campus.id
         left join graph_curso curso on gc.curso_id = curso.id
         left join graph_segmento segmento on pessoa.segmento_id = segmento.id
         left join graph_dimensao dimensao on pergunta.dimensao_id = dimensao.id
         left join graph_eixo eixo on dimensao.eixo_id = eixo.id;

refresh materialized view informacoes;
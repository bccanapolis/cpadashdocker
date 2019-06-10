create materialized view graph_view3 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece os resultados do último processo de autoavaliação institucional realizado pela Comissão Própria de Avaliação (CPA)?'
and part.resposta != 'N/A';

create materialized view graph_view4 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você participou do Planejamento do ano de 2018 na Pró-Reitoria a qual você está vinculado(a)?'
and part.resposta != 'N/A';

create materialized view graph_view5 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você participa da elaboração do Planejamento anual do seu Câmpus?'
and part.resposta != 'N/A';

create materialized view graph_view6 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você considera satisfatória a divulgação do Planejamento anual do seu Câmpus?'
and part.resposta != 'N/A';

create materialized view graph_view7 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Os cursos ofertados no seu Câmpus atendem as demandas socioeconômicas da região?'
and part.resposta != 'N/A';

create materialized view graph_view8 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'De maneira geral, você considera que a formação que está recebendo é de boa qualidade?'
and part.resposta != 'N/A';

create materialized view graph_view10 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você acompanha os trabalhos do Conselho de Ensino Pesquisa e Extensão (CONEPEX)?'
and part.resposta != 'N/A';

create materialized view graph_view11 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece ou participa de algum Projeto de Pesquisa do IFG?'
and part.resposta != 'N/A';

create materialized view graph_view12 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece ou participa de algum Projeto de Pesquisa do IFG?'
and part.resposta != 'N/A';

create materialized view graph_view13 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece ou participa de algum Projeto de Extensão do IFG?'
and part.resposta != 'N/A';

create materialized view graph_view14 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece ou participa de algum Projeto de Ensino?'
and part.resposta != 'N/A';

create materialized view graph_view15 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece ou participa de algum Projeto de Ensino?'
and part.resposta != 'N/A';

create materialized view graph_view16 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você considera satisfatória a atuação do IFG para promoção da permanência e êxito dos/das estudantes?'
and part.resposta != 'N/A';

create materialized view graph_view17 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você considera satisfatória a comunicação do IFG por meio do site e das redes sociais?'
and part.resposta != 'N/A';

create materialized view graph_view18 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece ou participa de algum Projeto de Pesquisa do IFG?'
and part.resposta != 'N/A';

create materialized view graph_view19 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'Você conhece a função da ouvidoria do IFG?'
and part.resposta != 'N/A';

create materialized view graph_view20 as
select pessoa.id         as pessoa,
       tema.titulo as tema,
       tema.id as tema_id,
       part.resposta as resposta,
       segmento.nome     as segmento,
       segmento.id as segmento_id,
       curso.nome as curso,
       curso.id as curso_id,
       campus.nome as campus,
        campus.id as campus_id
from graph_participacaopergunta as part
        left join graph_pergunta as pergunta on part.pergunta_id = pergunta.id
        left join graph_tema as tema on pergunta.tema_id = tema.id
         left join graph_pessoa as pessoa on part.pessoa_id = pessoa.id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         right join graph_pessoacurso gp on pessoa.id = gp.pessoa_id
         left join graph_curso as curso on gp.curso_id = curso.id
         left join graph_campus as campus on curso.campus_id = campus.id

where pergunta.titulo = 'De maneira geral, você é bem atendido/a nos setores de atendimento ao/à discente/docente no IFG?'
and part.resposta != 'N/A';


create materialized view graph_view1 as
select pessoa.id     as pessoa,
       campus.id as campus_id,
       campus.nome   as campus,
       segmento.nome as segmento,
       segmento.id as segmento_id
from graph_pessoa as pessoa
         left join graph_pessoacurso as pessoacurso on pessoa.id = pessoacurso.pessoa_id
         left join graph_segmento as segmento on pessoa.segmento_id = segmento.id
         left join graph_curso gc on pessoacurso.curso_id = gc.id
         left join graph_campus campus on gc.campus_id = campus.id;

select * from graph_view1
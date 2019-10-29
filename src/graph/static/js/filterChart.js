class FilterChart {
    constructor() {
        this.campus = new Array();
        this.cursos = new Array();
        this.graficos = new Array();
        this.chart = null;
        this.loadGraficos();
        this.loadSegmentos();
        this.loadLotacao();
        this.loadAtuacao();
    }

    loadGraficos() {
        $("#graficoChart").val(0);
        $.get("/api/grafico", result => {
            this.graficos = result.dados;
            this.appendGraficos();
            this.recreateChart();
            this.loadSegmentos();
        });
    }

    appendGraficos() {
        let grafico = $("#graficoChart");
        grafico.empty();
        this.graficos.forEach(item => {
            grafico.append(
                $("<option></option>")
                    .attr({value: item.id})
                    .text(`${item.titulo}`)
            );
        });
    }

    loadSegmentos() {
        $.get(`/api/segmento?pergunta=${$("#graficoChart").val() === '0' ? 1 : $("#graficoChart").val()}`, result => {
            this.segmentos = result.segmentos;
            this.appendSegmentos();
            this.loadCampus();
        });
    }

    appendSegmentos() {
        let segmentos = $("#segmentoChart");
        segmentos.empty();
        segmentos.append(
            $("<option></option>")
                .attr({value: 0, selected: true})
                .text(`Todos`)
        );
        this.segmentos.forEach(item => {
            segmentos.append(
                $("<option></option>")
                    .attr({value: item.id})
                    .text(`${item.nome}`)
            );
        });
    }

    loadAtuacao() {
        if ($("#campusChart").val() !== '0') {
            let reqSegmento = $("#segmentoChart").val() !== '0' ? `&segmento=${$("#segmentoChart").val()}` : ''
            $("#atuacaoChart").val(0)
            $.get(`/api/atuacao?pergunta=${$("#graficoChart").val()}&campus=${$("#campusChart").val()}${reqSegmento}`, result => {
                this.atuacao = result.atuacao;
                this.appendAtuacao();
            });
        }
    }

    appendAtuacao() {
        let atuacao = $("#atuacaoChart");
        atuacao.empty();
        atuacao.append(
            $("<option></option>")
                .attr({value: 0, selected: true})
                .text(`Todos`)
        );
        this.atuacao.forEach(item => {
            atuacao.append(
                $("<option></option>")
                    .attr({value: item.id})
                    .text(`${item.nome}`)
            );
        });
    }

    loadLotacao() {
        if ($("#campusChart").val() !== '0') {
            let reqSegmento = $("#segmentoChart").val() !== '0' ? `&segmento=${$("#segmentoChart").val()}` : ''
            $("#lotacaoChart").val(0)
            $.get(`/api/lotacao?pergunta=${$("#graficoChart").val()}&campus=${$("#campusChart").val()}${reqSegmento}`, result => {
                this.lotacao = result.lotacao;
                this.appendLotacao();
            });
        }
    }

    appendLotacao() {
        let lotacao = $("#lotacaoChart");
        lotacao.empty();
        lotacao.append(
            $("<option></option>")
                .attr({value: 0, selected: true})
                .text(`Todos`)
        );
        this.lotacao.forEach(item => {
            lotacao.append(
                $("<option></option>")
                    .attr({value: item.id})
                    .text(`${item.nome}`)
            );
        });
    }

    loadCampus() {
        $("#campusChart").val(0);
        $.get(`/api/campus?pergunta=${$("#graficoChart").val()}${$("#segmentoChart").val() !== '0' ? '&segmento=' + $("#segmentoChart").val() : ''}`, result => {
            this.campus = result.campus;
            this.appendCampus();
            this.loadCursos();
            this.loadAtuacao();
            this.loadLotacao();
            this.isCampusTodos();
        });
    }

    appendCampus() {
        let campus = $("#campusChart");
        campus.empty();
        campus.append(
            $("<option></option>")
                .attr({value: 0, selected: true})
                .text(`Todos`)
        );
        this.campus.forEach(item => {
            campus.append(
                $("<option></option>")
                    .attr({value: item.id})
                    .text(`${item.campus}`)
            );
        });
    }

    isCampusTodos() {
        if ($("#campusChart").val() == 0) {
            $("#cursoChart").attr({disabled: true});
            $("#atuacaoChart").attr({disabled: true});
            $("#lotacaoChart").attr({disabled: true});
        } else {
            $("#cursoChart").attr({disabled: false});
            $("#atuacaoChart").attr({disabled: false});
            $("#lotacaoChart").attr({disabled: false});
        }
    }

    appendCursos() {
        let cursos = $("#cursoChart");
        cursos.empty();
        cursos.append(
            $("<option></option>")
                .attr({value: 0, selected: true})
                .text(`Todos`)
        );
        this.cursos.forEach(item => {
            cursos.append(
                $("<option></option>")
                    .attr({value: item.id})
                    .text(`${item.nome}`)
            );
        });
    }

    loadCursos() {
        if ($("#campusChart").val() !== '0') {
             let reqSegmento = $("#segmentoChart").val() !== '0' ? `&segmento=${$("#segmentoChart").val()}` : ''
            $("#cursoChart").val(0);
            $.get(`/api/curso?campus=${$("#campusChart").val()}&pergunta=${$("#graficoChart").val()}${reqSegmento}`, result => {
                this.cursos = result.cursos;
                this.appendCursos();
                this.isCampusTodos();
            });
        }
    }

    updateChart(normal) {
        let curso = parseInt($("#cursoChart").val());
        let campus = parseInt($("#campusChart").val());
        let pergunta = parseInt($("#graficoChart").val());
        let atuacao = parseInt($("#atuacaoChart").val());
        let lotacao = parseInt($("#lotacaoChart").val());
        let segmento = parseInt($("#segmentoChart").val());
        this.isCampusTodos();
        this.chart.updateChart({pergunta, curso, campus, atuacao, lotacao, segmento}, normal);
    }

    recreateChart(normal) {
        $("#chart-place")
            .empty()
            .append(
                $('<div id="graph" class="ct-chart tc-chart ct-perfect-fourth"></div>')
            );
        this.chart = new ChartBar({pergunta: parseInt($("#graficoChart").val())}, "#graph", normal);
    }
}

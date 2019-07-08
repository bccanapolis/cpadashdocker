class FilterChart {
  constructor() {
    this.campus = new Array();
    this.cursos = new Array();
    this.graficos = new Array();
    this.chart = null;
    this.loadGraficos();
  }
  loadGraficos() {
    $("#graficoChart").val(0);
    $.get("/api/grafico", result => {
      this.graficos = result.graficos;
      this.appendGraficos();
      this.recreateChart();
      this.loadCampus();
    });
  }
  appendGraficos() {
    let grafico = $("#graficoChart");
    grafico.empty();
    this.graficos.forEach(item => {
      grafico.append(
        $("<option></option>")
          .attr({ value: item.numero })
          .text(`${item.titulo}`)
      );
    });
  }
  loadCampus() {
    $("#campusChart").val(0);
    $.get(`/api/campus?grafico=${$("#graficoChart").val()}`, result => {
      this.campus = result.campus;
      this.appendCampus();
      this.loadCursos();
    });
  }
  appendCampus() {
    let campus = $("#campusChart");
    campus.empty();
    campus.append(
      $("<option></option>")
        .attr({ value: 0, selected: true })
        .text(`Todos`)
    );
    this.campus.forEach(item => {
      campus.append(
        $("<option></option>")
          .attr({ value: item.id })
          .text(`${item.nome}`)
      );
    });
  }
  isCampusTodos() {
    if ($("#campusChart").val() == 0) {
      $("#cursoChart").attr({ disabled: true });
    } else {
      $("#cursoChart").attr({ disabled: false });
    }
  }
  appendCursos() {
    let cursos = $("#cursoChart");
    cursos.empty();
    cursos.append(
      $("<option></option>")
        .attr({ value: 0, selected: true })
        .text(`Todos`)
    );
    this.cursos.forEach(item => {
      cursos.append(
        $("<option></option>")
          .attr({ value: item.id })
          .text(`${item.nome}`)
      );
    });
  }
  loadCursos() {
    $("#cursoChart").val(0);
    $.get(`/api/curso?campus=${$("#campusChart").val()}&grafico=${$("#graficoChart").val()}`, result => {
      this.cursos = result.cursos;
      this.appendCursos();
      this.isCampusTodos();
    });
  }
  updateChart() {
    let curso = parseInt($("#cursoChart").val());
    let campus = parseInt($("#campusChart").val());
    let grafico = parseInt($("#graficoChart").val());
    switch (grafico) {
      case 1:
        this.chart.updateChart({ view: grafico, campus });
        break;
      default:
        this.chart.updateChart({ view: grafico, curso, campus }, campus != 0);
        break;
    }
  }
  recreateChart() {
    $("#chart-place")
      .empty()
      .append(
        $('<div id="graph" class="ct-chart tc-chart ct-perfect-fourth"></div>')
      );

    switch (parseInt($("#graficoChart").val())) {
      case 1:
        this.chart = new ChartPieRoles({ view: 1 }, "#graph", []);
        break;
      case 3:
        this.chart = new ChartBar({ view: 3 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 4:
        this.chart = new ChartBar({ view: 4 }, "#graph", [
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 5:
        this.chart = new ChartBar({ view: 5 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 6:
        this.chart = new ChartBar({ view: 6 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 7:
        this.chart = new ChartBar({ view: 7 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 8:
        this.chart = new ChartPie({ view: 8 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 10:
        this.chart = new ChartBar({ view: 10 }, "#graph", [
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 11:
        this.chart = new ChartPie({ view: 11 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 12:
        this.chart = new ChartBar({ view: 12 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo",
          "-Total"
        ]);
        break;
      case 13:
        this.chart = new ChartBar({ view: 13 }, "#graph", [
          "Docente",
          "Discente",
          "Técnico-Administrativo"
        ]);
        break;
      case 14:
        this.chart = new ChartPie({ view: 14 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 15:
        this.chart = new ChartBar({ view: 15 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo",
          "-Total"
        ]);
        break;
      case 16:
        this.chart = new ChartBar({ view: 16 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo",
          "-Total"
        ]);
        break;
      case 17:
        this.chart = new ChartBar({ view: 17 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 18:
        this.chart = new ChartPie({ view: 18 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo"
        ]);
        break;
      case 19:
        this.chart = new ChartBar({ view: 19 }, "#graph", [
          "Discente",
          "Docente",
          "Técnico-Administrativo",
          "-Total"
        ]);
        break;
      case 20:
        this.chart = new ChartBar({ view: 20 }, "#graph", [
          "Discente",
          "Docente"
        ]);
        break;
    }
  }
}

class TableChart {
  constructor(pergunta, data, roles) {
    this.data = data;
    this.view = pergunta;
    this.roles = roles;
    this.div = $("#tableChart");
    this.table = null;
    this.clearTable();
    this.instanciateTable();
  }
  clearTable() {
    this.div.empty();
  }
  instanciateTable() {
    this.table = new TableChartGen(this.data, this.roles)
  }
  static createTable(labels, data, indicator) {
    let thead = $("<thead></thead>");
    console.log(indicator)
    thead.attr('data-indicator', indicator);
    let trhead = $("<tr></tr>");
    labels.forEach(item => {
      trhead.append($("<th></th>").text(item));
    })
    let tbody = $("<tbody></tbody>");
    data.forEach(item => {
      let row = $("<tr></tr>");
      for (let col in item) {
        row.append($("<td></td>").text(item[col]))
      }
      tbody.append(row);
    })
    $("#tableChart").append(thead.append(trhead)).append(tbody);

  }
}
class TableChartRoles {
  constructor(data) {
    this.rawData = data;
    this.data = new Array();
    if($("#campusChart").val() == 0){
      this.sanitizeDataCampus();
    }else{
      this.sanitizeDataCurso();
    }
    
    TableChart.createTable(this.labels, this.data);
  }
  sanitizeDataCurso() {
    let total = 0;
    this.labels = ['Curso', 'Total', 'Porcentagem'] ;
    this.rawData.forEach(item => {
      total += item.count;
    })
    this.rawData.forEach(item => {
      this.data.push({ campus: item.curso, total: item.count, porcentagem: Math.round((item.count * 100 / total)*10)/10 + "%" })
    })
  }
  sanitizeDataCampus() {
    let total = 0;
    this.labels = ['Campus', 'Total', 'Porcentagem'];
    this.rawData.forEach(item => {
      total += item.count;
    })
    this.rawData.forEach(item => {
      this.data.push({ campus: item.campus, total: item.count, porcentagem: Math.round(item.count * 100 / total) + "%" })
    })
  }
}
class TableChartGen {
  constructor(data, roles) {
    this.rawData = data;
    this.roles = roles;
    this.labels = ['Segmento', 'Resposta', 'Total', 'Porcentagem'];
    this.data = new Array();
    this.indicador = 0;
    this.sanitizeData();
    TableChart.createTable(this.labels, this.data, this.indicador);
  }
  sanitizeData() {
    let ans = {}
    this.rawData.forEach(item => {
      if (typeof ans[item.segmento] == 'undefined' || ans[item.segmento] == null) {
        ans[item.segmento] = item.count;
      } else {
        ans[item.segmento] += item.count;
      }
    })

    this.rawData.forEach(item => {
      this.data.push({ segmento: item.segmento, resposta: item.resposta, total: item.count, porcentagem: Math.round((item.count * 100 / ans[item.segmento])*10)/10 + "%" })
    })
    this.data.sort((a,b) => (a.segmento > b.segmento) ? 1 : ((b.segmento > a.segmento) ? -1 : 0));

  }
}
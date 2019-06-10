class TableChart {
  constructor(view, data, roles) {
    this.data = data;
    this.view = view;
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
    switch (this.view) {
      case 1:
        this.table = new TableChartRoles(this.data);
        break;
      default:
        this.table = new TableChartGen(this.data, this.roles)
        break;
    }
  }
  static createTable(labels, data) {
    let thead = $("<thead></thead>");
    labels.forEach(item => {
      thead.append($("<th></th>").text(item));
    })
    let tbody = $("<tbody></tbody>");
    data.forEach(item => {
      let row = $("<tr></tr>");
      for (let col in item) {
        row.append($("<td></td>").text(item[col]))
      }
      tbody.append(row);
    })
    $("#tableChart").append(thead).append(tbody);
  }
}
class TableChartRoles {
  constructor(data) {
    this.rawData = data;
    this.labels = ['Campus', 'Total', 'Porcentagem'];
    this.data = new Array();
    this.sanitizeData();
    TableChart.createTable(this.labels, this.data);
  }
  sanitizeData() {
    let total = 0;

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
    this.sanitizeData();
    TableChart.createTable(this.labels, this.data);
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
      this.data.push({ segmento: item.segmento, resposta: item.resposta, total: item.count, porcentagem: Math.round(item.count * 100 / ans[item.segmento]) + "%" })
    })
  }
}
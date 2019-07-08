const unique = (value, index, self) => {
  return self.indexOf(value) === index;
}
class ChartGeneric {
  constructor(link, idDiv, roles) {
    this.link = link;
    this.div = idDiv;
    this.roles = roles;
    if (this.roles.includes("-Total")) {
      this.noTotal = true;
      this.roles = this.roles.filter(value => {
        return value != "-Total";
      });
    }
    this.series = null;
    this.labels = null;
    this.table = null;
  }
  updateRoles() {
    let roles = [];
    this.rawData.forEach(item => {
      roles.push(item.segmento);
    });
    this.roles = roles.filter(unique);
  }

  defaultOptions(colors = ["#3498db", "#e74c3c"]) {
    return {
      series: this.series,
      labels: this.labels,
      dataLabels: {
        enabled: true,
        formatter: function(val) {
          // index.w.config.series[0].data[index.dataPointIndex] +  index.w.config.series[0].data[index.dataPointIndex]
          return `${Math.ceil(val)}%`;
        }
      },
      tooltip: {
        y: {
          formatter: function(
            value,
            { series, seriesIndex, dataPointIndex, w }
          ) {
            return Math.round(value) + "%";
          }
        }
        // custom: function({ series, seriesIndex, dataPointIndex, w }) {
        //   return (
        //     "<div >" +
        //     "<span> Total: " + (this.rawData[1][dataPointIndex] + this.rawData[0][dataPointIndex]) +
        //     " </span><br><span> Porcentagem:" +
        //       series[seriesIndex][dataPointIndex] +
        //     "%</span>" +
        //     "</div>"
        //   );
        // }
      },
      toolbar: {
        show: false,
        tools: {
          download: false
        }
      },
      stroke: {
        show: true,
        width: 2,
        colors: ["transparent"]
      },
      colors: colors,
      fill: {
        colors: colors
      },
      fill: {
        opacity: 1
      }
    };
  }
  sanitizeRoles() {
    return this.roles.map(item => {
      return item
        .replace("-", " ")
        .split(" ")
        .map(word => {
          return (word += "s");
        })
        .join(" ");
    });
  }
  getDataAPI(info) {
    if(typeof info.campus == 'undefined' || info.campus == null){
      info.campus = 0;
    }
    if(typeof info.curso == 'undefined' || info.curso == null){
      info.curso = 0;
    }
    return new Promise((resolve, reject) => {
      $.get(`/cpa/api/grafico?view=${info.view}&curso=${info.curso}&campus=${info.campus}`, result => {
        this.table = new TableChart(info.view, result.data, this.roles);
        resolve(result.data);
      });
    });
  }
}

class ChartBar extends ChartGeneric {
  constructor(link, idDiv, roles) {
    super(link, idDiv, roles);
    super.labels = ["Sim", "Não"];
    this.getDataAPI(this.link)
      .then(data => {
        this.rawData = data;
        let res = this.sanitizeData(this.roles, this.rawData);
        super.series = [
          {
            name: "Sim",
            data: res[0]
          },
          {
            name: "Não",
            data: res[1]
          }
        ];
        this.chartInit();
      })
      .then(() => {
        this.render();
      });
  }
  render() {
    this.chart.render();
  }
  updateChart(link, noTotal) {
    this.link = link;
    this.getDataAPI(this.link).then(data => {
      this.rawData = data;
      this.updateRoles();
      this.noTotal = noTotal;
      this.series = this.sanitizeData(this.roles, this.rawData);
      this.chart.updateSeries(
        [
          {
            name: "Sim",
            data: this.series[0]
          },
          {
            name: "Não",
            data: this.series[1]
          }
        ],
        true
      );
      this.chart.updateOptions({
        xaxis: {
          categories: this.noTotal
            ? this.sanitizeRoles()
            : this.sanitizeRoles().concat("Total")
        }
      });
    });
  }
  chartInit() {
    this.chart = new ApexCharts(
      document.querySelector(this.div),
      Object.assign(super.defaultOptions(), {
        chart: {
          height: 350,
          type: "bar"
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "75%",
            endingShape: "rounded"
          }
        },
        xaxis: {
          categories: this.noTotal
            ? super.sanitizeRoles()
            : super.sanitizeRoles().concat(["Total"])
        },
        yaxis: {
          title: {
            text: "Porcentagem"
          }
        }
      })
    );
  }
  sanitizeData(roles, data) {
    let sim = new Array(roles.length).fill(0);
    sim[roles.length] = 0;
    let nao = new Array(roles.length).fill(0);
    nao[roles.length] = 0;

    data.forEach(item => {
      let rindex = roles.lastIndexOf(item.segmento);
      if (rindex != -1) {
        if (item.resposta == "Sim") {
          sim[rindex] = item.count;
          sim[roles.length] += sim[rindex];
        } else {
          nao[rindex] = item.count;
          nao[roles.length] += nao[rindex];
        }
      }
    });

    for (let i = 0; i < sim.length; i++) {
      let total = sim[i] + nao[i];
      sim[i] = Math.round((sim[i] * 100) / total);
      nao[i] = Math.round((nao[i] * 100) / total);
    }

    if (this.noTotal) {
      sim.pop();
      nao.pop();
    }
    return (this.series = [sim, nao]);
  }
}

class ChartPie extends ChartGeneric {
  constructor(link, idDiv, roles) {
    super(link, idDiv, roles);
    super.labels = ["Sim", "Não"];
    this.getDataAPI(this.link)
      .then(data => {
        this.rawData = data;
        super.series = this.sanitizeData(this.roles, this.rawData);
        this.chart = this.chartInit();
        
      })
      .then(() => {
        this.chart.render();
      });
  }
  updateChart(link) {
    this.link = link;
    this.getDataAPI(this.link).then(data => {
      this.rawData = data;
      this.updateRoles();
      this.noTotal = false;
      this.series = this.sanitizeData(this.roles, this.rawData);
      this.chart.updateSeries(
        this.series, true
      );
    });
  }
  sanitizeData(roles, data) {
    let sim = new Array(roles.length);
    sim[roles.length] = 0;
    let nao = new Array(roles.length);
    nao[roles.length] = 0;

    data.forEach(item => {
      let rindex = roles.lastIndexOf(item.segmento);
      if (rindex != -1) {
        if (item.resposta == "Sim") {
          sim[rindex] = item.count;
          sim[roles.length] += sim[rindex];
        } else {
          nao[rindex] = item.count;
          nao[roles.length] += nao[rindex];
        }
      }
    });
    let total = sim[roles.length] + nao[roles.length];
    sim[roles.length] = Math.round((sim[roles.length] * 100) / total);
    nao[roles.length] = Math.round((nao[roles.length] * 100) / total);
    return [sim[roles.length], nao[roles.length]];
  }
  chartInit() {
    return new ApexCharts(
      document.querySelector(this.div),
      Object.assign(super.defaultOptions(), {
        chart: {
          height: 400,
          type: "pie"
        },
        legend: {
          position: "right"
        },
        responsive: [
          {
            breakpoint: 600,
            options: {
              chart: {
                height: 480
              },
              legend: {
                position: "bottom"
              }
            }
          }
        ]
      })
    );
  }
}

class ChartPieRoles extends ChartGeneric {
  constructor(link, idDiv, roles) {
    super(link, idDiv, roles);
    this.getDataAPI(this.link)
      .then(data => {
        this.rawData = data;
        let res = this.sanitizeData(this.rawData);
        this.chartInit(res)
        
      })
      .then(() => {
        this.chart.render();
      });
  }
  updateChart(link) {
    this.link = link;
    this.getDataAPI(this.link).then(data => {
      
      this.rawData = data;
      this.updateRoles();
      this.noTotal = false;
      if($("#campusChart").val() == 0){
        this.series = this.sanitizeData(this.rawData);
        this.chart.updateOptions({
          labels: this.series.campus  
        });
      }else{
        this.series = this.sanitizeDataCurso(this.rawData);
        this.chart.updateOptions({
          labels: this.series.curso  
        });
      }
      
      this.chart.updateSeries(
        this.series.count, true
      );
    });
  }
  sanitizeDataCurso(data) {
    let curso = new Array();
    let count = new Array();
    let total = 0;

    data.forEach(item => {
      count.push(item.count);
      curso.push(item.curso);
      total += item.count;
    });

    count = count.map(item => {
      return Math.round((item * 100) / total);
    });
    return { curso, count };
  }
  sanitizeData(data) {
    let campus = new Array();
    let count = new Array();
    let total = 0;

    data.forEach(item => {
      count.push(item.count);
      campus.push(item.campus);
      total += item.count;
    });

    count = count.map(item => {
      return Math.round((item * 100) / total);
    });
    return { campus, count };
  }
  chartInit(res) {
    this.chart = new ApexCharts(
      document.querySelector(this.div),
      Object.assign(
        super.defaultOptions([
          "#F3B415",
          "#F27036",
          "#663F59",
          "#6A6E94",
          "#4E88B4",
          "#00A7C6",
          "#18D8D8",
          "#A9D794",
          "#46AF78",
          "#A93F55",
          "#8C5E58",
          "#2176FF",
          "#33A1FD",
          "#7A918D",
          "#BAFF29"
        ]),
        {
          chart: {
            height: 400,
            type: "pie"
          },
          legend: {
            position: "right"
          },
          labels: res.campus,
          series: res.count,
          responsive: [
            {
              breakpoint: 600,
              options: {
                chart: {
                  height: 480
                },
                legend: {
                  position: "bottom"
                }
              }
            }
          ]
        }
      )
    );
  }
}

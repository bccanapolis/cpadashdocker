const unique = (value, index, self) => {
    return self.indexOf(value) === index;
}

class ChartGeneric {
    constructor(link, idDiv, normal = false, total = false) {
        this.link = link;
        this.div = idDiv;
        this.series = null;
        this.labels = null;
        this.table = null;
        this.normal = normal;
        this.total = total;
    }

    normalize(series) {
        for (let i = 0; i < series[0].data.length; i++) {
            let sum = 0
            series.forEach(item => {
                sum += item.data[i]
            });
            for (let j = 0; j < series.length; j++) {
                series[j]['data'][i] = Math.round((series[j]['data'][i] / sum * 100) * 10) / 10
            }
        }
        return series
    }

    defaultOptions(colors = ['#008ffb', '#00e396', '#feb019', '#ff4560', '#775dd0', '#2e294e']) {
        let normal = this.normal
        return {

            legend: {
                position: 'bottom',
                offsetY: -10
            },
            series: this.series,
            labels: this.labels,
            dataLabels: {
                enabled: true,
                formatter: function (val) {
                    // index.w.config.series[0].data[index.dataPointIndex] +  index.w.config.series[0].data[index.dataPointIndex]
                    return `${val}`;
                }
            },
            tooltip: {
                followCursor: true,
                y: {
                    formatter: function (val) {
                        return normal ? `${val}%` : `${val}`;
                    }
                },
                x: {
                    show: true
                }
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
                colors: colors,
                opacity: 1
            }
        };
    }

    setIndicator(indicador) {
        this.indicator = indicador;
        let indicatorP = $("#chart-indicator").text(`${this.indicator.label} - ${this.indicator.valor}%`)
        indicatorP.css('background-color', this.indicator.cor)
    }

    getDataAPI(info) {
        let reqCampus = typeof info.campus != 'undefined' && info.campus != null && info.campus !== 0 ? `&campus=${info.campus}` : ''
        let reqCurso = typeof info.curso != 'undefined' && info.curso != null && info.curso !== 0 ? `&curso=${info.curso}` : ''
        let reqAtuacao = typeof info.atuacao != 'undefined' && info.atuacao != null && info.atuacao !== 0 ? `&atuacao=${info.atuacao}` : ''
        let reqLotacao = typeof info.lotacao != 'undefined' && info.lotacao != null && info.lotacao !== 0 ? `&lotacao=${info.lotacao}` : ''
        let reqSegmento = typeof info.segmento != 'undefined' && info.segmento != null && info.segmento !== 0 ? `&segmento=${info.segmento}` : ''
        // console.table(info)
        return new Promise((resolve, reject) => {
            $.get(`api/grafico?pergunta=${info.pergunta}${reqSegmento}${reqAtuacao}${reqLotacao}${reqCampus}${reqCurso}`, result => {
                if (info.pergunta != 0) {
                    this.setIndicator(result.indicador)
                    this.table = new TableChart(info.pergunta, result.data, this.roles);
                }
                this.roles = result.roles;
                // this.labels = result.respostas;
                resolve(result.data);
            });
        });
    }
}

class ChartBar extends ChartGeneric {
    constructor(link, idDiv, normal, total) {
        super(link, idDiv, normal, total);
        super.labels = ['Ótimo', 'Bom', 'Regular', 'Ruim', 'Péssimo', 'Não sei'];
        this.getDataAPI(this.link)
            .then(data => {
                this.rawData = data;
                super.series = this.sanitizeData(this.labels, this.rawData);

                this.chartInit();
            })
            .then(() => {
                this.render();
            });
    }

    render() {
        this.chart.render();
    }

    updateChart(link, normal, total) {
        if (typeof normal !== 'undefined' && normal !== null) {
            this.normal = normal
        }
        if (typeof total !== 'undefined' && total !== null) {
            this.total = total
        }
        this.link = link;
        this.getDataAPI(this.link).then(data => {
            this.rawData = data;
            this.chart.updateSeries(
                this.sanitizeData(this.labels, this.rawData),
                true
            );
            this.chart.updateOptions({
                xaxis: {
                    categories: this.roles
                },
                yaxis: {
                    title: {
                        text: this.normal ? "Porcentagem" : "Pessoas"
                    }
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
                    type: "bar",
                    // stacked: true,
                    columnWidth: '90%'
                },
                plotOptions: {
                    bar: {
                        horizontal: false,
                        endingShape: 'rounded',
                        columnWidth: '98%'
                    }
                },
                xaxis: {
                    categories: this.roles
                },
                yaxis: {
                    title: {
                        text: this.normal ? "Porcentagem" : "Pessoas"
                    }
                }
            })
        );
    }

    sanitizeData(labels, data) {
        let series = {};
        let total = {}
        labels.forEach(item => {
            series[item] = {name: item, data: new Array(this.roles.length).fill(0)}
        })
        data.forEach(item => {
            series[item.resposta].data[this.roles.lastIndexOf(item.segmento)] = item.count
        })
        let final = []
        if (this.total && this.roles.length > 1) {
            for (let [key, value] of Object.entries(series)) {
                let sum = 0
                for (let i = 0; i < value.data.length; i++) {
                    sum += value.data[i]
                }
                series[key].data.push(sum)

            }
            this.roles.push('Total')
        }
        for (let [key, value] of Object.entries(series)) {
            final.push(value)
        }

        if (this.normal) {
            final = this.normalize(final)
        }
        return final
    }
}

class ChartPie extends ChartGeneric {
    constructor(link, idDiv, normal, total) {
        super(link, idDiv, normal, total);
        this.getDataAPI(this.link)
            .then(data => {
                this.rawData = data;
                super.series = this.sanitizeData(this.roles, this.rawData);
                this.chartInit();
            })
            .then(() => {
                this.render();
            });
    }

    render() {
        this.chart.render();
    }

    updateChart(link, normal, total) {
        if (typeof normal !== 'undefined' && normal !== null) {
            this.normal = normal
        }
        if (typeof total !== 'undefined' && total !== null) {
            this.total = total
        }
        this.link = link;
        this.getDataAPI(this.link).then(data => {
            this.rawData = data;
            this.chart.updateSeries(
                this.sanitizeData(this.roles, this.rawData),
                true
            );
            this.chart.updateOptions({
                labels: this.roles
            });
        });
    }

    sanitizeData(labels, data) {
        let final = new Array(labels.length).fill(0)
        data.forEach(item => {
            final[labels.lastIndexOf(item.label)] = item.count
        })
        return final
    }

    chartInit() {
        this.chart = new ApexCharts(
            document.querySelector(this.div),
            Object.assign(super.defaultOptions([
                "#008ffb","#00e396","#feb019","#ff4560","#775dd0","#ff9800","#4caf50",
                "#03a9f4","#3f51b5","#546e7a","#d4526e","#13d8aa","#a5978b","#fd6a6a",
                "#546e7a","#4ecdc4","#449dd1","#f9a3a4","#fa4443","#662e9b", "#e2c044",
                "#f86624","#5c4742","#8d5b4c","#a5978b","#5653fe","#c4bbaf","#2e294e"
            ]), {
                chart: {
                    height: 400,
                    type: "pie"
                },
                legend: {
                    position: "right"
                },
                labels: this.roles,
                series: this.series,
                dataLabels: {
                    enabled: true,
                    formatter: function (val) {
                        return Math.round(val * 10) / 10 + "%"
                    },
                }
            })
        );
    }
}

// class ChartPieRoles extends ChartGeneric {
//   constructor(link, idDiv, roles) {
//     super(link, idDiv, roles);
//     this.getDataAPI(this.link)
//       .then(data => {
//         this.rawData = data;
//         let res = this.sanitizeData(this.rawData);
//         this.chartInit(res)
//
//       })
//       .then(() => {
//         this.chart.render();
//       });
//   }
//   updateChart(link) {
//     this.link = link;
//     this.getDataAPI(this.link).then(data => {
//
//       this.rawData = data;
//       this.updateRoles();
//       this.noTotal = false;
//       if($("#campusChart").val() == 0){
//         this.series = this.sanitizeData(this.rawData);
//         this.chart.updateOptions({
//           labels: this.series.campus
//         });
//       }else{
//         this.series = this.sanitizeDataCurso(this.rawData);
//         this.chart.updateOptions({
//           labels: this.series.curso
//         });
//       }
//
//       this.chart.updateSeries(
//         this.series.count, true
//       );
//     });
//   }
//   sanitizeDataCurso(data) {
//     let curso = new Array();
//     let count = new Array();
//     let total = 0;
//
//     data.forEach(item => {
//       count.push(item.count);
//       curso.push(item.curso);
//       total += item.count;
//     });
//
//     count = count.map(item => {
//       return Math.round((item * 100) / total);
//     });
//     return { curso, count };
//   }
//   sanitizeData(data) {
//     let campus = new Array();
//     let count = new Array();
//     let total = 0;
//
//     data.forEach(item => {
//       count.push(item.count);
//       campus.push(item.campus);
//       total += item.count;
//     });
//
//     count = count.map(item => {
//       return Math.round((item * 100) / total);
//     });
//     return { campus, count };
//   }
//   chartInit(res) {
//     this.chart = new ApexCharts(
//       document.querySelector(this.div),
//       Object.assign(
//         super.defaultOptions(),
//         {
//           chart: {
//             height: 400,
//             type: "pie"
//           },
//           legend: {
//             position: "right"
//           },
//           labels: res.campus,
//           series: res.count,
//           responsive: [
//             {
//               breakpoint: 600,
//               options: {
//                 chart: {
//                   height: 480
//                 },
//                 legend: {
//                   position: "bottom"
//                 }
//               }
//             }
//           ]
//         }
//       )
//     );
//   }
// }

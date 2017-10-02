import React from 'react';
import Highcharts from 'highcharts';

class DevicePieChart extends React.Component {
  componentDidMount() {
    this.drow(this.props)
  }

  componentWillReceiveProps(nextProps, nextState) {
    this.chart.destroy()
    this.drow(nextProps)
  }

  shouldComponentUpdate() {
  	return false
  }

  componentWillUnmount() {
    this.chart.destroy()
  }

  drow(props) {
	 this.chart = Highcharts.chart(this.container, {
      chart: {
        type: 'pie',
      },
      title: {
        text: props.title
      },
      
      tooltip: {
        pointFormat: '<span style="color:{series.color}">{series.name}</span>: {point.y:,.0f}<br/>',
        split: true
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
              enabled: true,
              format: '{point.name}: {point.y:.1f}%'
          }
      }
      },
      series: [
        {
          name: 'Browser',
          data: props.data
        }
      ]
    })
  }

  render() {
    return <div className="chart" ref={ref => this.container = ref} />
  }
}


export default DevicePieChart;
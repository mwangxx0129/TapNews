import React from 'react';
import Highcharts from 'highcharts';

class ActiveUserChart extends React.Component {
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
        type: 'line'
      },
      title: {
        text: props.title
      },
      xAxis: {
       categories: [
        'Monday',
        'Tuesday',
        'Wedensday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
      ],
        tickmarkPlacement: 'on',
        title: {
          enabled: false
        }
      },
      yAxis: {
        title: {
          text: 'Operation Number'
        }
      },
      tooltip: {
        pointFormat: '<span style="color:{series.color}">{series.name}</span>: {point.y:,.0f}<br/>',
        split: true
      },
      plotOptions: {
        area: {
          stacking: 'hello',
          lineColor: '#ffffff',
          lineWidth: 1,
          marker: {
            lineWidth: 1,
            lineColor: '#ffffff'
          }
        }
      },
      series: props.data
    })
  }

  render() {
    return <div className="chart" ref={ref => this.container = ref} />
  }
}


export default ActiveUserChart;
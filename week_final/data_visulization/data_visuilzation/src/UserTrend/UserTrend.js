import React from 'react';
import Highcharts from 'highcharts';

class UserTrend extends React.Component {
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
        type: 'column'
      },
      title: {
        text: props.title
      },
      xAxis: {
       categories: [
        '00:00',
        '01:00',
        '02:00',
        '03:00',
        '04:00',
        '05:00',
        '06:00',
        '07:00',
        '08:00',
        '09:00',
        '10:00',
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00',
        '18:00',
        '19:00',
        '20:00',
        '21:00',
        '22:00',
        '23:00'
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


export default UserTrend;
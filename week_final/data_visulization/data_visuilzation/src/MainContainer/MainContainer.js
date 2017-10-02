import React, { Component } from 'react';
import PanelHeader from '../PanelHeader/PanelHeader.js';
import Panel from '../Panel/Panel.js';
import Range from '../Range/Range.js';

import UserTrend from '../UserTrend/UserTrend.js';
import ActiveUserChart from '../ActiveUserChart/ActiveUserChart.js';
import DevicePieChart from '../DevicePieChart/DevicePieChart.js';
import NewsCategory from '../NewsCategory/NewsCategory.js';

const category = ['technology', 'music', 'education','sports','politics', 'weather','others'];

class MainContainer extends React.Component{
    constructor(){
        super();
        this.state = {
            user_trend: null,
            user_device: null,
            user_news_category: null,
            user_active_time: null
        };
    }

    componentDidMount(){
        this.loadUserTrend();
        this.loadUserDevice();
        this.loadNewsCategory();
        this.loadUserActiveTime();
    }

    loadUserTrend(){
        let url = 'http://localhost:8080/userdata/usertrend';
        let request = new Request(url, {
            method: 'GET',
            cache: false
        });

        fetch(request)
            .then((res)=>res.json())
            .then((userTrend) => {
                this.setState({
                    user_trend: userTrend
                });
            })
    }

    loadUserDevice(){
        let url = 'http://localhost:8080/userdata/userdevice';
        let request = new Request(url, {
            method: 'GET',
            cache: false
        });

        fetch(request)
            .then((res)=>res.json())
            .then((userDevice) => {
                this.setState({
                    user_device: userDevice
                });
            })
    }

    loadNewsCategory(){
        let url = 'http://localhost:8080/userdata/newscategory';
        let request = new Request(url, {
            method: 'GET',
            cache: false
        });

        fetch(request)
            .then((res)=>res.json())
            .then((newscategory) => {
                this.setState({
                    user_news_category: newscategory
                });
            })
    }
    
    loadUserActiveTime(){
        let url = 'http://localhost:8080/userdata/activetime';
        let request = new Request(url, {
            method: 'GET',
            cache: false
        });

        fetch(request)
            .then((res)=>res.json())
            .then((activetime) => {
                this.setState({
                    user_active_time: activetime
                });
            })
    }

    render(){
        return(
            <div>
                <div className="row">
                    <div className="col-md-5 custom_padding" >
                        <Panel>
                            <PanelHeader title="User Device">
                            </PanelHeader>
                            <DevicePieChart data={this.state.user_device}/>
                        </Panel>
                    </div>
                    <div className="col-md-7 custom_padding" >
                        <Panel>
                            <PanelHeader title="User Trend (Daily Active/Daily New)">
                            </PanelHeader>
                            <div>
                            <ActiveUserChart data={this.state.user_trend} />
                            </div>
                        </Panel>
                    </div>
                </div>
                <br/>
                <br/>
                <br/>
                <div className = "row">
                    <div className="col-md-7 custom_padding" >
                            <Panel>
                                <PanelHeader title="Daily Active Time">
                                </PanelHeader>
                                <UserTrend data={this.state.user_active_time} />
                            </Panel>
                    </div>
                    <div className="row">
                        <div className="col-md-5 custom_padding" >
                            <Panel>
                                <PanelHeader title="News Category">
                                </PanelHeader>
                            <NewsCategory data = {this.state.user_news_category}/>
                                
                            </Panel>
                        </div>

                    </div>
                </div>
            </div>
        );
    };

};

export default MainContainer;
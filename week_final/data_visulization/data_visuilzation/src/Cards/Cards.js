import React from 'react';
import SingleCard from '../SingleCard/SingleCard.js';
import Range from '../Range/Range.js';

// const user_data = [
//     {
//         'title': 'Total Users',
//         'num':1300
//     },
//     {
//         'title': 'New Users',
//         'num':23
//     },
//     {
//         'title': 'Active Users',
//         'num':67
//     },
//     {
//         'title': 'Average Reading',
//         'num':12
//     }
// ];

const colors=['#53c79f','#64b0cc','#7a6fca','#ca6f96'];

class Cards extends React.Component {
    constructor(){
        super();
        this.state = {
            user_data: null,
            colors:null
        };
    }

    componentDidMount(){
        this.loadUserData();
    }

    loadUserData() {
        // console.log('setState');
        let url = 'http://localhost:8080/userdata/statistic';
        let request = new Request(url, {
            method: 'GET',
            cache: false
        });

        fetch(request)
            .then((res)=>res.json())
            .then((userdata) => {
                this.setState({
                    user_data: userdata,
                });
            })

        this.setState({
            colors:colors
        });
        console.log(this.state.colors);
    }

    renderUserData() {
        console.log('render-- singleCard');
        const user_list = this.state.user_data.map((user,index)=>{
            return (
                <SingleCard user={user} color={colors[index]}/>
            );
        });

        return(
            <div className = 'row'>
                {user_list}
            </div>
        );
    }

    render(){
        if(this.state.user_data){
            console.log('render user data');
            return(
                <div>
                    {this.renderUserData()}
                </div>
            );
        } else {
            return(
                <div>
                    <h1> LOADING...</h1>
                </div>
            );
        }
    }
}

export default Cards;
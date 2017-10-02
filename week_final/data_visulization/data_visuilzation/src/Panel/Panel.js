import React from 'react';
import  './Panel.css';

class Panel extends React.Component{
    render(){
        return(
            <div className = "bg">
                {this.props.children}
            </div>  
        );
    }
}

export default Panel;
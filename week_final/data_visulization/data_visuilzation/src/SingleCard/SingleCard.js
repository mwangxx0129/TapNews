import React from 'react';
import './SingleCard.css';


class SingleCard extends React.Component {

    render(){
        var style = {
            backgroundColor:this.props.color
        };
        return(
            <div className="col-xs-3 custom_padding margin-below-20" >
            <div className="card" style={style}>
                <div className="card_header">
                    <div className="pull-left">
                        {this.props.user.title}
                    </div>
                </div>
                <hr className="hr-custom"/>
                <div className="card_body">
                    {this.props.user.num}
                    
                </div>
            </div>
        </div>
        );
    }
}

export default SingleCard;
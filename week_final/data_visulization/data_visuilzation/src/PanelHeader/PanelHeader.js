import React from 'react';
import  './PanelHeader.css';

class PanelHeader extends React.Component {
    render(){
        return(
            <div className="panel-header">
            <div className="pull-left panel-title">{this.props.title}</div>
            <div className="pull-right line-height-30">
                {this.props.children}
            </div>

        </div>
        );
    };
}

PanelHeader.propTypes = {
    title: React.PropTypes.string
}

export default PanelHeader;
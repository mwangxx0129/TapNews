import React, { Component } from 'react';
import './Range.css';

class Range extends Component {
  render() {
    return (
        <div>
            <span className="range-span">
                <svg width="10" height="10">
                    <circle cx="5" cy="5" r="5" fill="#e58c72"/>
                </svg>
                <span className="padding-left-5">Today</span>
            </span>
            <span className="range-span">
                <svg width="10" height="10">
                    <circle cx="5" cy="5" r="5" fill="#8f8f8f"/>
                </svg>
                <span className="padding-left-5">7 days</span>
            </span>
        </div>
    );
  }
}

export default Range;
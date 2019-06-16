import React from 'react';
import { Link } from 'react-router-dom'

import { PLAYITEM_STATUSES } from '../../constants';

import "../../stylesheets/PlayItem.css"


const PlayItem = props => {

    const thumb_path = '/images/thumbs/' + props.playitem.thumb

    return (
        <div className="playitem">
            <div className="playitem-header">
                <div>
                    { props.playitem.name }
                </div>
                <select value={ props.playitem.status } onChange={ onStatusChange }>
                    { PLAYITEM_STATUSES.map(status => (
                          <option key={ status } value={ status }>
                              { status }
                          </option>
                      )) }
                </select>
            </div>
            <div className="playitem-body">

                <Link to={{pathname: "/player" , state:{url: props.playitem.url} }} >

                { props.playitem.url }
                </Link>

            </div>
            <img src="/images/loading.gif" data-echo={ thumb_path } />
            { props.playitem.thumb && <div className="playitem-body">
                                          { props.playitem.thumb_resolution }
                                      </div> }
            <hr />
        </div>
        );

    function onStatusChange(e) {
        props.onStatusChange(props.playitem.id, e.target.value);
    }
};

export default PlayItem;

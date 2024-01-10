import React from 'react'
import '../HomeCSS/Component1.css';

import Salesforce from '../images/Salesforce.jpg';

function Component1() {
  return (

        <nav className='main'>

            <div className="logo">
                <img src={Salesforce} className='image_logo'/>
            </div>
            <div className='links'>
                <ul className='unordered'>
                    <li className='list'>
                        <a>HOME</a>
                    </li>
                    <li className='list'>
                        <a>ABOUT</a>
                    </li>
                    <li className='list'>
                        <a>CAREERS</a>
                    </li>
                    <li className='list'>
                        <a>DEVELOPMENT</a>
                    </li>
                </ul>
            </div>

            <div className='right_link'>

            </div>

        </nav>

  )
}

export default Component1
import React, { useState } from 'react'
import {api} from '../assets/apikey.js'
import Clock from './Clock';

const CurrTime = () => {
  return (
    <div className='section'>
      <Clock />
    </div>
  )
}

export default CurrTime;
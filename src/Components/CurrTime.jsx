import React, { useState } from 'react'
import {api} from '../assets/apikey.js'
import Clock from './Clock';

const URL = `https://api.openweathermap.org/data/2.5/weather?q=${location}&units=imperial&appid=${api}`;

const CurrTime = () => {
  return (
    <div className='section'>
      <Clock />
    </div>
  )
}

export default CurrTime;
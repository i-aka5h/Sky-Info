import React, { useEffect, useState } from "react";

let currDate = new Date();
let currTime = currDate.toLocaleTimeString();

const dateToday = () => {
    let months = [
        "January",
        "Febuaray",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ];
    let days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];
    let currDate = new Date();
    let day = days[currDate.getDay()];
    let date = currDate.getDate();
    let month = months[currDate.getMonth()];
    let year = currDate.getFullYear();

    return `${day}, ${date} ${month} ${year}`;
}

const Clock = () => {
    const [timeNow, setTimeNow] = useState(currTime);

    const updateTime = () => {
        setTimeNow(new Date().toLocaleTimeString())
    };
    useEffect(() => {
        setInterval(() => {
            updateTime()
        }, 1000)
    }, []
    )

    return (
        <>
            <p>{timeNow}</p>
            <p>{dateToday()}</p>
        </>
    )
}

export default Clock;
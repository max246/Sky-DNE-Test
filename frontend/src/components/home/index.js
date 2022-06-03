import React, { useRef, useState } from "react";
import config from '../../config'
import List from "../list/index";


function Home(props) {
    const [valueID, setID] = useState(0);
    const [valueIP, setIP] = useState(0);

    const handleChange = (e) => {
     const value = e.currentTarget.value;
     const id = e.currentTarget.id;
     if (id === "id") setID(value)
     else setIP(value)
    }

    const handleAdd = () => {
        const response = fetch(config.api + "loopback/add", {
            method: "POST",
            cache: "no-cache",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                id: valueID,
                ip: valueIP
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                    console.log("done",data)
            });
    }

    return <>
        <h1>List interfaces</h1>
        <List/>
        <h1>Add loopback</h1>
       ID : <input type="text" value={valueID}  onChange={handleChange} id="id" name="id"/>
        IP: <input type="text" value={valueIP}  onChange={handleChange} id="ip" name="ip"/>
        <button type="button" onClick={handleAdd} name="button">Add</button>
    </>;
}

export default Home;

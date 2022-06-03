import React, {useState} from "react";
import config from "../../config";
import {useEffect} from "react";

function List(props) {
    const [interfaces, setInterfaces] = useState([]);

    const handleDel = (id, ip) => {
        console.log(id,ip)
        const response = fetch(config.api + "loopback/del", {
            method: "POST",
            cache: "no-cache",

            headers: {
                "Content-Type": "application/json",
                'Access-Control-Allow-Origin':'http://localhost:5050',
            },
            body: JSON.stringify({
                id: id,
                ip: ip
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log("done",data)
            });
        return true
    }

    useEffect(() => {
        fetch(config.api )
            .then(res => res.json())
            .then((data) => {
                console.log(data)
                setInterfaces(data.list)
            })
    },[])

    return <>
        {interfaces.map((item, i) => {
            return (<div>ID: {item[0]} | IP: {item[1]}  <a href="#" onClick={() => { handleDel(item[0], item[1])}} >Delete</a> </div>)
        })}
    </>;
}

export default List;

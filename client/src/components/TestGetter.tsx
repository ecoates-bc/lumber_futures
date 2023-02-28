import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";

export default function TestGetter() {
    let [res, setRes] = useState("Waiting for result...");

    useEffect(() => {
        axios.get("http://localhost:8000/futures/")
            .then((response) => {
                console.log(response);
                setRes(JSON.stringify(response.data));
            })
            .catch((err) => {
                setRes("Error: unable to get result.")
            });
    }, []);

    return (
        <p>{res}</p>
    );
}
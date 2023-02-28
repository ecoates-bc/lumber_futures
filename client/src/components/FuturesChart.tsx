import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import { ResponsiveContainer, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Line } from "recharts";

import CategorySelector from "./CategorySelector";

export default function FuturesChart() {
    const [status, setStatus] = useState("loading");
    const [data, setData] = useState([]);
    const [category, setCategory] = useState("Open");

    useEffect(() => {
        axios.get("http://localhost:8000/futures/")
            .then((response) => {
                if (response.status === 200) {
                    setData(response.data);
                    setStatus("loaded");
                } else {
                    setStatus("error");
                }
            })
            .catch((err) => {
                setStatus("error");
            });
    }, []);

    if (status === "loading") {
        return (
            <h2>Loading data...</h2>
        );
    } else if (status === "loaded") {
        return (
            <>
                <CategorySelector onChange={setCategory}/>
                <ResponsiveContainer
                    width="100%"
                    aspect={3}
                >
                    <LineChart
                        data={data}
                        margin={{
                            top: 5,
                            right: 30,
                            left: 20,
                            bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="1 1" />
                        <XAxis dataKey="Date" interval={15}/>
                        <YAxis />
                        <Tooltip />
                        <Line type="linear" dataKey={category} strokeWidth={5}/>
                    </LineChart>
                </ResponsiveContainer>
            </>
        );
    } else {
        return (
            <h2>Error: unable to import data from server.</h2>
        );
    }
}
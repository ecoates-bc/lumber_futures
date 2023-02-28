import React from "react";

type CategorySelectorProps = {
    onChange: (txt: string) => void;
};

export default function CategorySelector(props: CategorySelectorProps) {
    return (
        <h2>
            <label>Category: </label>
            <select
                onChange={e => props.onChange(e.target.value)}
            >
                <option value="Open">Open</option>
                <option value="High">High</option>
                <option value="Low">Low</option>
                <option value="Close">Close*</option>
                <option value="Adj_Close">Adj Close**</option>
                <option value="Volume">Volume</option>
            </select>
        </h2>
    );
}
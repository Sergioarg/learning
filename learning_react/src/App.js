import { useState } from 'react';
import Apples from "./components/Apples";
import Bag from "./components/Bag";
import Card from "./components/Card";
import Heading from "./components/Heading";
import Pears from "./components/Pears";
import MealList from './components/MealsList';
import MealsProvider from './providers/MealsProvider';
import Fruits from "./components/Fruits";
import React from 'react';
import FruitsCounter from './components/FruitsCounter';

function App() {
    const [fruits] = React.useState([
        { fruitName: 'apple', id: 1 },
        { fruitName: 'apple', id: 2 },
        { fruitName: 'plum', id: 3 },
    ]);

    const [name, setWord] = useState('Peter');

    function handleClick() {
        setWord('Parker');
    }


    return (
        <div className="App">

            <h1>Where should the state go?</h1>
            <Fruits fruits={fruits} />
            <FruitsCounter fruits={fruits} />


            <Heading firstName={name} />


            <Card h2="First card's h2" h3="First card's h3" />
            <button onClick={handleClick}>Click to change the name </button>

            <Bag children={<Apples color="yellow" number="5" />} />
            <Bag children={<Pears friend="Peter" />} />
        </div>
    );
};

export default App;

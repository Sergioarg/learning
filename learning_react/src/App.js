import Apples from "./components/Apples";
import Bag from "./components/Bag";
import Card from "./components/Card";
import Heading from "./components/Heading";
import Fruits from "./components/Fruits";
import React from 'react';
import FruitsCounter from './components/FruitsCounter';
import { Routes, Route, Link } from 'react-router-dom';

function App() {
    const [fruits] = React.useState([
        { fruitName: 'apple', id: 1 },
        { fruitName: 'apple', id: 2 },
        { fruitName: 'plum', id: 3 },
    ]);

    return (
        <div className="App">
            <nav>
                <Link to="/" className='nav-item'>Home Page</Link>
                <Link to="/bag" className='nav-item'>Bag </Link>
            </nav>
            <Routes>
                <Route path='/' element={<Heading firstName='Home Page' />}></Route>
                <Route path='/bag' element={<Bag children={<Apples color="yellow" number="5" />} />}></Route>
            </Routes>

            <h1>Where should the state go?</h1>
            <Fruits fruits={fruits} />
            <FruitsCounter fruits={fruits} />

            <Card h2="First card's h2" h3="First card's h3" />
        </div>
    );
};

export default App;

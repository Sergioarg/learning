import Apples from "./components/Apples";
import Bag from "./components/Bag";
import Card from "./components/Card";
import Heading from "./components/Heading";
import Pears from "./components/Pears";


function App() {


    return (
        <div className="App">
            <h1>Task: Add three Card elements</h1>
            <Card h2="First card's h2" h3="First card's h3" />
            <Card h2="Second card's h2" h3="Second card's h3" />
            <Card h2="Third card's h2" h3="Third card's h3" />

            <Heading firstName="Bob"/>
            <Bag children={<Apples color="yellow" number="5" />} />
            <Bag children={<Pears friend="Peter" />} />
        </div>
    );
};

export default App;

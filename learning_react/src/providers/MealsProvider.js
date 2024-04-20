import React from "react";

// Crea el ContextProvider
const MealsContext = React.createContext();

const todayMeals = ["Baked Beans", "Baked Sweet Potatoes", "Baked Potetoes"]

// Componte que recibe el componente hijo que va a recibir los datos
const MealsProvider = ({children}) => {

    const [meals, setMealsList] = React.useState(todayMeals);

    return (
        <MealsContext.Provider value={{meals}}>
            {children}
        </MealsContext.Provider>
    )
}

export const useMealsListContext = () => React.useContext(MealsContext);

export default MealsProvider;

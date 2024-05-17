// Question 10
// What would be printed on console when the following code snippet is run?

import React from 'react';

const MyComponent = (data) => {
    console.log(data);
    return (
        <div>
            {/. Some JSX ./}
        </div>
    );
};

const data = {
    apple: 1,
    mango: 2,
    banana: 3
}

ReactDON. render(
    <MyComponent { ... data} />,
    document.getElementById("container")
);

// Options
//* c. {apple: 1, mango: 2, banana: 3}

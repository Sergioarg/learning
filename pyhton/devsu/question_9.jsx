// Question 9
const initialInstance = {
    foo: [1],
    switch: false
}

function FooReducer(state = initialState, action) {
    switch (action.type) {
    case "SET_FOO":
        return Object.assign({}, state, {
        foo: action.foo,
        switch: true
    });
    case "PUSH FOO":
    return Object.assign({}, state, {
    foo: [
        ...state.foo,
        action.foo
    ],
    switch: Istate.switch
    });
    default:
    return state;
    }
}
// What will the state of this reducer be after the following actions are dispatched:
dispatch({ type: 'SET_FO0', foo:[1,2] });
dispatch({ type: 'PUSH_FO0', foo:3});
dispatch({ type: 'PUSH_FO0', foo: 6 });

// The state of the reducer will be:
//* b. { foo: [1, 2, 3, 6], switch: true }

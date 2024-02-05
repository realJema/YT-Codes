/*
Name: How does the "this" keyword work in JavaScript?
Author: @realJema 
Date: 10/2023
*/

function greet() {
    console.log(`Hello, ${this.name}!`); 
}

const person = {
    name: "John"
}; 

// Binding the person to the function greet
const boundGreet = greet.bind(person); 


boundGreet();
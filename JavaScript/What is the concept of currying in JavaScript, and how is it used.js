/*
Name: What is the concept of currying in JavaScript, and how is it used? 
Author: @realJema 
Date: 10/2023
Descr: The concept of currying in JavaScript refers to the process of transforming a function with multiple arguments into a sequence of functions, each taking a single argument. It allows you to create specialized versions of a function by partially applying its arguments. 
*/

// Currying a function 
function multiply(a) {
    return function(b) {
        return a * b; 
    }; 
}

// creating a specialized version of multiply
const multiplyByTwo = multiply(2); 

// Using the specialized version 
console.log(multiplyByTwo(5)); // Output: 10
console.log(multiplyByTwo(8)); // Output: 16
console.log(multiplyByTwo(11)); // OUtput: 22
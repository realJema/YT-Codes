/*
Name: Explain the differences between "let," "const," and "var" in JavaScript with example 
Author: @realJema 
Date: 10/2023
*/

// var example 
// with var, the variable has a function scope and redeclaring it within a block does not create a separate scope
var x = 10; 
if (true) {
    var x = 20; 
    console.log(x); // Output: 20
}
console.log(x); // Output: 20 

// let example 
// with let the variable has block scope meaning it is limited to the block in which it is defined
let y = 10; 
if (true) {
    let y = 20; 
    console.log(y); // Output: 20 
}
console.log(y); // Output: 10 

// const example 
// with const the variable also has block scope but it additionally cannot be reassigned after declaration
const z = 10; 
if (true) {
    const z = 20; 
    console.log(z); // Output: 20 
}
console.log(z); // Output: 10 
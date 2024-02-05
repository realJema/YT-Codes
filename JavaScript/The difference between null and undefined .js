/*
Name: The difference between null and undefined 
Author: @realJema 
Date: 10/2023
*/

// console.log(z); // ReferenceError: z is not defined 

var a = undefined; 
console.log(a); // Output: undefined 

var b = null; 
console.log(b); // Output: null 

console.log(undefined === null); // Output: false 
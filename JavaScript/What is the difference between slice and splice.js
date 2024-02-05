/*
Name: What is the difference between slice and splice
Author: @realJema 
Date: 10/2023
*/


const fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']; 

// Using slice : contains elements from index 1 to index 3 excluding the element at index 4
const slicedFruits = fruits.slice(1, 4);
console.log(slicedFruits); // Output: ['banana', 'cherry', 'date']; 

// Using splice : removes two elements starting from index 2 and inserts news ones in their place
const removedFruits = fruits.splice(2, 2, 'grape', 'fig'); 
console.log(removedFruits); // Output: ['cherry', 'date']; 
console.log(fruits); // Output: ['apple', 'banana', 'grape', 'fig', 'elderberry']; 
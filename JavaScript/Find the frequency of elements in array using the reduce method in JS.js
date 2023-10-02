
/*
 Name: Find the frequency of elements in array using the reduce method in JS
 Author: @realJema 
 Date: 07/2023
*/ 

const array = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1] // we start with our array with duplicate elements

const frequency = array.reduce((acc, curr) => { // create two objects to store the values
    if (curr in acc) { // we check if it exists as a key in the accumulator object
        acc[curr]++; // we increment its value in the accumulator
    } else { // we create the value in the accumulator 
        acc[curr] = 1; // we initialize its value 
    }
    return acc; 
}, {}); 

console.log(frequency); 
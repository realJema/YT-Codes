/*
Name:   function to apply the Bubble Sort algorithm.
Author: @realJema 
Date: 08/2023
*/

function bubbleSort(arr) {
    const length = arr.length; 

    for (let i = 0; i < length - 1; i++) {
        for (let j = 0; j < length - 1 - i; j++) {
            if (arr[j] > arr[j+1]){
                // swap elements 
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; 
            }
        }
    }

    return arr; 
}

// Example 
const array = [5, 3, 8, 4, 2, 1, 2, 234, 23, 19, 93]; 
const sortedArray = bubbleSort(array); 
console.log(sortedArray); 
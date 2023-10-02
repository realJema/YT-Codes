/*
Name: Write a JavaScript program for binary search. 
Author: @realJema 
Date: 08/2023
*/

function binarySearch(arr, target) {
    let start = 0; 
    let end = arr.length - 1; 

    while (start <= end) {
        let mid = Math.floor((start + end) / 2);

        // if target is found, return its index
        if (arr[mid] === target) {
            return mid; 
        }
        // if target is greater, ignore left harlf
        if (arr[mid] < target) {
            start = mid + 1; 
        }
        // if target is smaller, ignore right half
        else {
            end = mid - 1; 
        }
    }
    // if target is not found, return -1 
    return -1; 
}

// Example 
const sortedArray = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]; 
const targetValue = 20; 

const result = binarySearch(sortedArray, targetValue);
if(result !== -1) {
    console.log('Element ' + targetValue + ' found at index ' + result); 
} else {
    console.log('Element not found'); 
}
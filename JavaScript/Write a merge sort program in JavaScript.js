/*
Name:  Write a merge sort program in JavaScript.  
Author: @realJema 
Date: 08/2023
*/

function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr; 
    }

    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid); 
    const right = arr.slice(mid); 

    return merge(mergeSort(left), mergeSort(right)); 
}

function merge(left, right) {
    let result = []; 
    let leftIndex = 0; 
    let rightIndex = 0; 

    while (leftIndex < left.length && rightIndex < right.length) {

        if (left[leftIndex] <= right[rightIndex]) {
            result.push(left[leftIndex]);
            leftIndex++;
        } else {
            result.push(right[rightIndex]);
            rightIndex++; 
        }
    }

    return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex)); 
}

// example 
const array = [8, 4, 2, 9, 11, 45, 39, -2, 30, 5, 1, 6, 3, 7]
const sortedArray = mergeSort(array); 
console.log(sortedArray); 
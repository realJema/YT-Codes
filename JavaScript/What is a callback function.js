/*
Name: What is a callback function
Author: @realJema 
Date: 10/2023
*/

// Example function with a callback : its a function that is passed as an argument to another function and is executed at a later point in time or when a certain event occurs
function fetchData(callback) {
    setTimeout(() => {
        const data = {name: 'John', age: 30}; 
        callback(data); // Execute the callback function 
    }, 2000); 
}

// Callback function 
function processResult(data) {
    console.log(data); // Output: {name: 'John', age: 30}
}

// Calling function with callback 
fetchData(processResult); 
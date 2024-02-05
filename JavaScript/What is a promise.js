/*
Name: What is a promise
Author: @realJema 
Date: 10/2023
*/

// Function which returns a promise : A promise is an object in JS that represents the eventual completion (or failure) of an asynchronous operation and its resulting value
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = { name: 'John', age: 30}; 
            if (data){
                resolve(data); 
            } else {
                reject('Error occurred'); 
            }
        }, 2000); 
    })
}

// Consuming the promise 
fetchData()
    .then(data => {
        console.log(data); // Output: { name: 'John', age: 30}
    }) 
    .catch(error => {
        console.log(error); // Output: Error occurred
    })
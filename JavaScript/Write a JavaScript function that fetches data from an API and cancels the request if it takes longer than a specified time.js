/*
Name: Write a JavaScript function that fetches data from an API and cancels the request if it takes longer than a specified time.
Author: @realJema 
Date: 09/2023
*/

function fetchDataWithTimeout(url, timeout) {
    const controller = new AbortController(); 
    const { signal } = controller; 

    const timeoutId = setTimeout(() => {
        controller.abort(); 
    }, timeout); 

    return fetch(url, { signal })
        .then((response) => {
            clearTimeout(timeout); 
            if(!response.ok){
                throw new Error(response.statusText);
            }
            return response.json(); 
        })
        .catch((error) => {
            if(error.name === 'AbortError') {
                console.log('Request times out'); 
            } else {
                console.error('Error"', error); 
            }
        }); 
}

// Example 
const url = 'https://jsonplaceholder.typicode.com/posts'
const timeout = 1000; // time in milliseconds  

fetchDataWithTimeout(url, timeout)
    .then((data) => {
        console.log('Fetched data: ', data); 
    }); 
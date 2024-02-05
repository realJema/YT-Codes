/*
Name: How does "async/await" work in JavaScript?
Author: @realJema 
Date: 10/2023
*/

// Aschnchronous function using async/await 
function fetchData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('Data has been fetched'); 
        }, 2000); 
    }); 
}

async function getData() {
    try {
        const result = await fetchData(); 
        console.log(result); // OUtput: Data has been fetched
    } catch (error) {
        console.log(error); 
    }
}

getData(); 
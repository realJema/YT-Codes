/*
Name: Write a JavaScript a function that makes an HTTP GET request and returns a Promise that resolves with the response data.
Author: @realJema 
Date: 09/2023
*/
 

function makeGetRequest(url) {
    return new Promise((resolve, reject) => {
        var XMLHttpRequest = require('xhr2');
      const xhr = new XMLHttpRequest();
      xhr.open("GET", url);
  
      xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
          resolve(xhr.responseText);
        } else {
          reject(new Error(xhr.statusText));
        }
      };
  
      xhr.onerror = function () {
        reject(new Error("An error occurred during the request."));
      };
  
      xhr.send();
    });
  }
  
  // Example usage
  const url = "https://api.example.com/data";
  makeGetRequest(url)
    .then((response) => {
      console.log("Response data:", response);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
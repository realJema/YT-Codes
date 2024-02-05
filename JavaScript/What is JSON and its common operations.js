/*
Name: What is JSON and its common operations
Author: @realJema 
Date: 10/2023
*/


const jsonStr = '{"name": "John", "age": 30}';
const obj = JSON.parse(jsonStr); 
console.log(obj.name);   // Output: John 
console.log(obj.age); // Output: 30 

const obj2 = {name : 'John', age: 30}; 
const jsonStr2 = JSON.stringify(obj2); 
console.log(jsonStr2); 

const obj3 = {name: 'John', age: 30}
console.log(obj3.name); // Output: John
console.log(obj3['age']); // Output: 30

// updating values in json 
const obj4 = {name: 'John', age: 30};
obj4.age = 31; // Modifying age property
console.log(obj4.age); // Output: 31

// printing all values in json 
const obj5 = {name: 'John', age: 30};
for (let key in obj5) {
    console.log(key + ': ' + obj5[key]); 
}
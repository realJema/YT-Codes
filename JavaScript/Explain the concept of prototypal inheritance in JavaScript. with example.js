/*
Name: Explain the concept of prototypal inheritance in JavaScript. with example
Author: @realJema 
Date: 10/2023
*/

// Parent object constructor 
function Animal(name) {
    this.name = name; 
}

// Adding a method to the parent object's prototype 
Animal.prototype.sayHello = function() {
    console.log("Hello, I'm " + this.name); 
}; 

// Child object constructor 
function Dog(name, breed) {
    Animal.call(this, name); 
    this.breed = breed; 
}

// Inheriting properties and methods from the prototype
Dog.prototype = Object.create(Animal.prototype); 


// Adding a method specific to the child object 
Dog.prototype.bark = function() {
    console.log("Woof! I'm a " + this.breed); 
}; 

// Creating an instance of the child object 
var myDog = new Dog("Max", "Labrador"); 

// Accessing the child objects's specific method 
myDog.bark(); // Output: Woof! I'm a Labrador
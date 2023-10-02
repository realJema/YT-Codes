/*
Name: Write a JavaScript program to get the volume of a cylindrical with four decimal places using object classes.
Author: @realJema 
Date: 09/2023
*/

class Cyclinder {
    constructor(radius, height) {
        this.radius = radius; 
        this.height = height; 
    }

    getVolume() {
        const volume = Math.PI * Math.pow(this.radius, 2) * this.height; 
        return volume.toFixed(4); 
    }
}

// Example 
const myClinder = new Cyclinder(30, 50); 
const volume = myClinder.getVolume(); 
console.log("Volume of the cyclinder:", volume); 
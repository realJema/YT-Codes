/*
Name: Write a JavaScript program to calculate circle area and perimeter using objects
Author: @realJema 
Date: 06/2023
*/

class Circle {
    constructor(radius) {
        this.radius = radius; 
    }

    getArea() {
        const area = Math.PI * Math.pow(this.radius, 2); 
        return area.toFixed(4); 
    }

    getPerimeter() {
        const perimeter = 2 * Math.PI * this.radius; 
        return perimeter.toFixed(4); 
    }
}

// Example 
const myCircle = new Circle(15); 
const area = myCircle.getArea(); 
const perimeter = myCircle.getPerimeter(); 
console.log("Area of the circle: ", area); 
console.log("Perimeter of the circle: ", perimeter); 
/*
Name: Explain the concept of closures in JavaScript and provide an example.
Code: AI Generated 
Author: @realJema 
Date: 10/2023
Descr: closures are a powerful concept that allows functions to remember and access the variables from the scope in which they were created even when they are executed outside of that scope. 
*/

function outerFunction() {
    var outerVariable = 'Hello'; 

    function innerFunction() {
        var innerVariable = 'World'; 
        console.log(outerVariable + ' ' + innerVariable); 
    }

    return innerFunction; 
}

var closureExample = outerFunction();
closureExample(); 
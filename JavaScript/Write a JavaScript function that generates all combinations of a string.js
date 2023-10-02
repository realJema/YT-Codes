/*
Name: Write a JavaScript function that generates all combinations of a string.
Author: @realJema 
Date: 06/2023
*/

function generateCombinations(string) {
    let combinations = []; 

    function bacttrack(combination, remaining) {
        if (remaining.length === 0){
            combinations.push(combination)
        } else {
            for (let i = 0; i < remaining.length; i++) {
                let newCombination = combination + remaining[i]; 
                let newRemaining = remaining.slice(0, i) + remaining.slice(i + 1); 
                bacttrack(newCombination, newRemaining); 
            }
        }
    }

    bacttrack('', string); 
    return combinations; 
}

console.log(generateCombinations('abc'))
console.log(generateCombinations('word'))
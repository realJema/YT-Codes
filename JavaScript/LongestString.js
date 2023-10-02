/*
Name: 
    Find the longest increasing subsequence. Given a sequence of numbers, find the longest subsequence of numbers that are in increasing order. For example, the longest increasing subsequence in the sequence [1, 4, 2, 1, 5, 3, 6, 7] is [1, 4, 2, 5, 6, 7].
Code: JavaScript
Author: @realJema 
Date: 06/2023
*/ 

function findLongestIncreasingSubsequence(sequence) {
  const n = sequence.length;
  const lengths = Array(n).fill(1);
  const previousIndices = Array(n).fill(-1);
  let longestSubsequence = [];

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (sequence[i] > sequence[j] && lengths[i] < lengths[j] + 1) {
        lengths[i] = lengths[j] + 1;
        previousIndices[i] = j;
      }
    }
  }

  let maxLengthIndex = 0;
  for (let i = 1; i < n; i++) {
    if (lengths[i] > lengths[maxLengthIndex]) {
      maxLengthIndex = i;
    }
  }

  let index = maxLengthIndex;
  while (index >= 0) {
    longestSubsequence.unshift(sequence[index]);
    index = previousIndices[index];
  }

  return longestSubsequence;
}

const sequence = [1, 4, 2, 1, 5, 3, 6, 7];
const result = findLongestIncreasingSubsequence(sequence);
console.log(result); // Output: [1, 4, 5, 6, 7]
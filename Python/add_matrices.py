'''
name: add_matrices.py
author: realjema
date: 01/2023
'''

X = [[1,2,3],
    [4,5,6],
    [7,9,9]]

Y = [[9,12,7],
    [6,5,4],
    [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#iterate through rows
for i in range(len(X)):
    # now iterate through columns 
    for j in range(len(X[0])):
        result[i][j] = X[i][j] +  Y[i][j]  #the value in position result[i][j] is the sum of the equivalent positions in both X and Y


for r in result: 
    print(r)
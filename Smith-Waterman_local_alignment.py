# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:20:37 2023

@author: MDTus


#def smith_waterman_local_alignment(string_one, string_two, match, missMatch, gap):
    
    Parameters
    ----------
    string_one : String
        Frist String.
    string_two : String
        Second String.
    match : Int
        Point if match.
    missMatch : Int
        Point if miss matched.
    gap : Int
        point if a gap.
        
    Returns
    -------
    string
        Frist String.
    string
        Second String.
    2D List
        Needleman–Wunsch Matrix.
    Exampel
    --------
    needleman_wunshch_global_alignment(
        string_one(stringObject), 
        string_two(stringObject), 
        match(intObject), missMatch(intObject), gap(intObject)
    )
    Note
    ---
    
    """
# Collain Function
string_one = input("Please enter the first string: ")
string_two = input("Please enter the second string: ")
match = int(input("Match Poing: "))
missMatch = int(input("Missmatch Point: "))
gap = int(input("Gap Poing: "))


# finding the length of the strings
cols, rows = (len(string_one)+1, len(string_two)+1)

# Defineng Metrix
matrix = [[0 for i in range(cols)] for j in range(rows)]
# Matrix for back traking
track = [[-1 for i in range(cols)] for j in range(rows)]
# Creating string use token
token1 = list(range(cols-1))
token2 = list(range(rows-1))
maxValue = -1

# Calculating the Needleman-Wunsch matrix
for i in range(1, rows):
    for j in range(1, cols):
        if string_two[i-1] == string_one[j-1] :
            corner = ('corner', matrix[i-1][j-1] + match)
        else:
            corner = ('corner', matrix[i-1][j-1] + missMatch)
        left = ('left', matrix[i][j-1] + gap)
        top = ('top', matrix[i-1][j] + gap)
        maximum = max(corner[1], left[1], top[1])
        if maximum == corner[1] :
            track[i][j] = (i-1, j-1)
        elif maximum == left[1]:
            track[i][j] = (i, j-1)
        else:
            track[i][j] = (i-1, j)
        # making the max value 0 if it is a negative value
        if maximum > 0:
            maxValue = max(maxValue, maximum) # finding the maximum value
            matrix[i][j] = maximum
        
# This will print the matrix
for i in range(rows):
    for j in range (cols):
        print(matrix[i][j], end=' ')
    print()

# Thie will print the track matrix
for i in range(rows):
    for j in range (cols):
        print(track[i][j], end=' ')
    print()
print(maxValue)
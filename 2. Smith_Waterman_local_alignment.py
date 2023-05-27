# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:20:37 2023

@author: MDTus

"""
def smith_waterman_local_alignment(string_one, string_two, match, missMatch, gap):
    """
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
    pare value
        contains pare of strings 
    2D List
        Smith Waterman Matrix.
    Exampel
    --------
    smith_waterman_local_alignment(
        string_one(stringObject), 
        string_two(stringObject), 
        match(intObject), missMatch(intObject), gap(intObject)
    )
    Note
    ---
    
    """
    # For storing result
    
    # finding the length of the strings
    cols, rows = (len(string_one)+1, len(string_two)+1)
    # cols = length of the first string
    # rows = length of the second string
    
    # Defineng Metrix
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    # Matrix for back traking
    track = [[-1 for i in range(cols)] for j in range(rows)]
    
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
            if maximum >= 0:
                # finding the maximum value for backtracking
                maxValue = max(maxValue, maximum)
                # matrix value
                matrix[i][j] = maximum
            elif maximum < 0:
                track[i][j] = (None, None)
            
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
    
    
    # Finding the position where the max value present
    locations = list()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == maxValue :
                temp = (i, j)
                locations.append(temp)
    
    # Chossing the last max value location
    locationsLen = len(locations)
    
    maxloc = locations[locationsLen-1]
    # Creating string use token
    token1 = list(range(cols-1))
    token2 = list(range(rows-1))
    # Back Tracking
    solution_string_one = string_one[maxloc[1]-1]
    solution_string_two = string_two[maxloc[0]-1]
    token1[maxloc[1]-1] = None
    token2[maxloc[0]-1] = None
    index_one = track[maxloc[0]] [maxloc[1]][1]
    index_two = track[maxloc[0]] [maxloc[1]][0]
        
    length = max(len(string_one), len(string_two)) - 1
    
    while length :
        if track[index_one] == None or track[index_two] == None:
            break
        if index_one == 0 and index_two == 0:
            break
        
        if (index_one - 1) in token1 :
            solution_string_one = (
                string_one[index_one - 1] + solution_string_one
            )
            index = token1.index((index_one - 1))
            token1[index] = None
        else :
            solution_string_one = '_' + solution_string_one
        
        if (index_two - 1) in token2 :
            solution_string_two = (
                string_two[index_two - 1] + solution_string_two
            )
            index = token2.index((index_two - 1))
            token2[index] = None
        else :
            solution_string_two = '_' + solution_string_two
        
       
        temp1 = index_one
        temp2 = index_two
        
        if temp1 and temp2 :
            index_one = track[temp2][temp1][1]
            index_two = track[temp2][temp1][0]
        else:
            break
            
        length -= 1
    
    # Minimizing Cost
    # String One
    length = len(solution_string_one)
    count = solution_string_one.count('_')
    i = 0
    while count :
        j = solution_string_one.index('_', i)
        k = j;
        count_ = 0
        for f in range(j, length):
            if solution_string_one[f] == '_':
                count_ += 1
                k += 1
            else: 
                break
        
        for l in range(j, k):
            if solution_string_two[l] == solution_string_one[k]:
                temp = list(solution_string_one)
                temp[l] = temp[k]
                temp[k] = '_'
                solution_string_one = "".join(temp)
                break
        i = k+1
        count -= count_
    # String Two
    length = len(solution_string_two)
    count = solution_string_two.count('_')
    i = 0
    while count :
        j = solution_string_two.index('_', i)
        k = j;
        count_ = 0
        for f in range(j, length):
            if solution_string_two[f] == '_':
                count_ += 1
                k += 1
            else: 
                break
        
        for l in range(j, k):
            if solution_string_one[l] == solution_string_two[k]:
                temp = list(solution_string_two)
                temp[l] = temp[k]
                temp[k] = '_'
                solution_string_two = "".join(temp)
                break
        i = k+1
        count -= count_
    
    # Formating Result
    temp1 = list(solution_string_one)
    temp2 = list(solution_string_two)
    
    solution_string_one = " ".join(temp1)
    solution_string_two = " ".join(temp2)
    
    result = (solution_string_one, solution_string_two)
    
        
    return result, matrix
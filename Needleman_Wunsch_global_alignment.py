# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:49:05 2023

@author: MD. Imrul Kayes
@University: Chittangong University of Engineering and Technology (CUET)

Project: Needleman-Wunsch Global Alignment
------------------------------------------

"""
def needleman_wunshch_global_alignment(string_one, string_two, match, missMatch, gap):
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
    """
    
    # finding the length of the strings
    cols, rows = (len(string_one)+1, len(string_two)+1)
    
    # Defineng Metrix
    matrix = [[None for i in range(cols)] for j in range(rows)]
    # Matrix for back traking
    track = [[-1 for i in range(cols)] for j in range(rows)]
    # Creating string use token
    token1 = list(range(cols-1))
    token2 = list(range(rows-1))
    
        
    # Processing the first row and the first column of the matrix
    matrix[0][0] = 0
    for i in range(rows):
        for j in range (cols):
            if i == 0 and j > 0:
                matrix[i][j] = matrix[i][j-1] + gap
            if i > 0 and j == 0:
                matrix[i][j] = matrix[i-1][j] + gap
            # print(matrix[i][j], end=' ')
        # print()
    
    
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
            matrix[i][j] = maximum
            
    # This will print the matrix
    # for i in range(rows):
    #     for j in range (cols):
    #         print(matrix[i][j], end=' ')
    #     print()
    
    # Thie will print the track matrix
    # for i in range(rows):
    #     for j in range (cols):
    #         print(track[i][j], end=' ')
    #     print()
            
    
    # Back Tracking
    solution_string_one = string_one[cols-2]
    solution_string_two = string_two[rows-2]
    token1[token1.index(cols-2)] = None
    token2[token2.index(rows-2)] = None
    index_one = track[rows-1][cols-1][1]
    index_two = track[rows-1][cols-1][0]
    
    length = max(len(string_one), len(string_two)) - 1
    
    while length :
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
    cols -= 1
    rows -= 1
    
    if (cols > rows) :
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
    else:
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
            
            
    temp1 = list(solution_string_one)
    temp2 = list(solution_string_two)
    
    solution_string_one = " ".join(temp1)
    solution_string_two = " ".join(temp2)
    
    return solution_string_one, solution_string_two, matrix


# printing Matrix function
def print_needleman_wunsch_matrix(matrix, length_one, length_two):
    '''
    Parameters
    ----------
    matrix : 2D list
        Needleman–Wunsch Matrix.
    length_one : Int
        lenth of the first string.
    length_two : int
        length of the second string.

    Returns
    -------
    None.

    '''
    length_one += 1
    length_two += 1
    for i in range(length_two):
        for j in range (length_one):
            print(matrix[i][j], end=' ')
        print()
    print()



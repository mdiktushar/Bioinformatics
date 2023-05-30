# -*- coding: utf-8 -*-
"""
Created on Mon May  29 17:28:41 2023

@author: MDTus
"""

# intervals = [(1, 5, 4), (3, 9, 3), (4, 10, 3), (7, 13, 6), 
#              (10, 17, 10), (11, 16, 2), (14, 19, 1), (17, 19, 8)]
intervals = [(1, 5, 5), (2, 3, 3), (4, 8, 6), (6, 12, 10), (7, 17, 12), 
            (9, 10, 1), (11, 15, 7), (13, 14, 0), (16, 18, 4)]
'''
Textbook example
intervals = [(1, 5, 5), (2, 3, 3), (4, 8, 6), (6, 12, 10), (7, 17, 12), 
            (9, 10, 1), (11, 15, 7), (13, 14, 0), (16, 18, 4)]
'''
##############################################################################

# Generates a few useful dictionaries and lists from the intervals in input

    # Dictionary where keys = right coordinates and values = left coordinates
right2left = {val[1]: val[0] for k, val in enumerate (intervals)}

    # Dictionary where keys = right coordinates and values = weights
right2weight = {val[1]: val[2] for k, val in enumerate (intervals)}

    # Ordered list of the right coordinates
rights = []
for k, val in enumerate (intervals):
    rights.append (val [1])
    rights.sort ()

    # List of weights
weights = []
for k, val in enumerate (intervals):
    weights.append (val [2])

    # Initializes a scores list
scores = [0] * (max(rights))

# Defines a small function to "pad" a list (I will use it on the scores list)
 # "Pads" a list i.e. fill it with 'value' from 'start' position up to the end
def pad (any_list, value, start):
    i = len(any_list) + 1
    while i > start:
        any_list [i - 2] = value
        i -=1
    return any_list

####################################

# Main loop of dynamical programming. It generates the scores list.
previous_score = 0

for r in rights:
    '''
    computes the possible new score = 
                        score at the left coordinate + weight of the interval
    '''
    possible_new_score = scores[right2left [r] - 1] + right2weight [r]
    new_score = max (previous_score, possible_new_score)
    pad (scores, new_score, r)
    previous_score = new_score

# Backtracking from the scores list to generate the path
    # i.e. the intervals we followed to get to the maximum score
path = []
right = len(scores)

while right > 0:
    
    # is 'right' an actual right coordinate of an interval?
    if right in right2left: 
        left = right2left [right]
        weight = right2weight [right]
        # 'test_score' because we are going to test 
        # it against the score we have in the scores list
        test_score = scores [left - 1] + weight
        
        # if 'test_score' is equal to the score we have at this position,
        # then we have used this interval
        if test_score == scores [right - 1]: 
            # inserts in 'path' the interval we followed
            path.insert (0, [left, right, weight])
            # left coordinate of this interval becomes right coordinate 
            # for the next iteration of the while loop
            right = left 

        else: 
            # if 'test_score' is not equal to the score we have,
            # backtrack one position and try again
            right -= 1

    else: 
        # if 'right' is not in 'right2left',
        # backtrack one position and try again
        right -= 1

##############################################################################
# OUTPUT

# print statements
print ('\nMaximum score: ', max(scores))
print ('Path in the graph (intervals used): ', path)
print ('>intervals format [left coordinate, right coordinate, weight]')


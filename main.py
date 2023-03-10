# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 02:20:15 2023

@author: MD. Imrul Kayes
@University: Chittangong University of Engineering and Technology (CUET)
"""

from Needleman_Wunsch_global_alignment import *

# Collain Function
string_one = input("Please enter the first string: ")
string_two = input("Please enter the second string: ")
match = int(input("Match Poing: "))
missMatch = int(input("Missmatch Point: "))
gap = int(input("Gap Poing: "))

string1, string2, matrix = needleman_wunshch_global_alignment(string_one, string_two, match, missMatch, gap)
print_needleman_wunsch_matrix(matrix, len(string_one), len(string_two))
print(string1, string2, sep='\n')

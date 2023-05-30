# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:53:49 2023
@author: MDTus
"""

import math

def partial_Digest(L, n):

	max_element_in_List, solution = max(L), []
	solution.append(0)

	# while L is not empty
	while L:

		# gets the maximum distance of L
		max_dist = max(L)

		x1, x2 = max_element_in_List - max_dist, max_dist
		x1_chosen, x2_chosen = True, True
		diff_dists_x1, diff_dists_x2 = [], []

		# checks if x1 is a valid choice
		for i in solution:
			dist = abs(i - x1)
			diff_dists_x1.append(dist)
			if dist not in L:
				x1_chosen = False
				break

		# if x1 not is a valid choice
		if not x1_chosen:
			# checks if x2 is a valid choice
			for i in solution:
				dist = abs(i - x2)
				diff_dists_x2.append(dist)
				if dist not in L:
					x2_chosen = False
					break

		# checks the choices
		if not x1_chosen and not x2_chosen:
			return None
		else:
			if x1_chosen:
				solution.append(x1) # add solution
				for dist in diff_dists_x1: # removes the distances
					L.remove(dist)
			else:
				solution.append(x2) # add solution
				for dist in diff_dists_x2: # removes the distances
					L.remove(dist)

	solution.sort() # sort numbers
	return solution # return the solution


L = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]
len_L = len(L)

	# |D| = (n * (n-1)) / 2
	# n^2 - n - 2 * len_l = 0
	# n = (1 + sqrt(1 + 8 * len_l)) / 2
delta = math.sqrt(1 + 8 * len_L)
n = (1 + delta) / 2

solution = partial_Digest(L, int(n))
print(solution)


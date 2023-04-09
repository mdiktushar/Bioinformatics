# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:48:54 2023

@author: MDTus
"""

def HammingDistance(s1, s2):
    # Function to compute Hamming distance between two strings
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance = distance + 1
    return distance

def RecursiveBranchAndBound(kmer, distance, depth):
    global bestDistance, bestKmer, DNA, n, l
    if depth == l:
        # Reached the end of the k-mer, compute total Hamming distance
        totalDistance = 0
        for dna in DNA:
            minDistance = float('inf')
            for i in range(n - l + 1):
                substring = dna[i:i+l]
                dist = HammingDistance(kmer, substring)
                if dist < minDistance:
                    minDistance = dist
            totalDistance = totalDistance + minDistance
        if totalDistance < bestDistance:
            bestDistance = totalDistance
            bestKmer = kmer
    else:
        # Continue branching
        for nucleotide in ['A', 'C', 'G', 'T']:
            newKmer = kmer + nucleotide
            newDistance = distance + 1
            if newDistance < bestDistance:
                RecursiveBranchAndBound(newKmer, newDistance, depth + 1)

# Initialize bestDistance and bestKmer
bestDistance = float('inf')
bestKmer = ""

# Start the recursive Branch and Bound search
DNA = ["AGTC", "AGTT", "AGCT"]  # Input list of DNA strings
t = len(DNA)  # Number of DNA strings
n = len(DNA[0])  # Length of each DNA string
l = 3  # Desired length of median string (k-mer)

RecursiveBranchAndBound("", 0, 0)

# Print the result
print("Median string with minimum Hamming distance:", bestKmer)

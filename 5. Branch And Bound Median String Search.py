# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:02:13 2023

@author: MDTus
"""

def hamming_distance(str1, str2):
    """
    Calculates the Hamming distance between two strings of equal length.
    """
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

def total_distance(pattern, dna):
    """
    Calculates the total distance between a pattern and a list of DNA strings.
    """
    k = len(pattern)
    distance = 0
    for string in dna:
        min_hamming = float('inf')
        for i in range(len(string) - k + 1):
            kmer = string[i:i+k]
            hamming = hamming_distance(pattern, kmer)
            if hamming < min_hamming:
                min_hamming = hamming
        distance += min_hamming
    return distance

def median_string(dna, k):
    """
    Finds the median string of length k that minimizes the total distance to a list of DNA strings using Branch and Bound.
    """
    distance = float('inf')
    median = ""

    def calculate_bound(pattern, level):
        """
        Calculates the lower bound for the current partial pattern.
        """
        bound = 0
        for string in dna:
            min_hamming = float('inf')
            for i in range(len(string) - k + 1):
                kmer = string[i:i+k]
                hamming = hamming_distance(pattern, kmer)
                if hamming < min_hamming:
                    min_hamming = hamming
            bound += min_hamming
            if bound >= distance:
                return distance  # Prune the branch if the bound is already larger than the current best distance
        return bound

    def backtrack(pattern, level):
        nonlocal distance, median
        if level == k:
            pattern_distance = total_distance(pattern, dna)
            if pattern_distance < distance:
                distance = pattern_distance
                median = pattern
            return

        bound = calculate_bound(pattern, level)
        if bound >= distance:
            return  # Prune the branch if the bound is already larger than the current best distance

        for nucleotide in "ACGT":
            new_pattern = pattern + nucleotide
            backtrack(new_pattern, level + 1)

    backtrack("", 0) # Start the backtrack process with an empty pattern and level 0
    return median # Return the median string that minimizes the total distance



# Example usage
dna_strings = ["ACGT", "AGGT", "ACTT", "ACCT"]
# dna_strings = ["AAACTCAAACCC", "AAACACGGGCCC", "AAACPCAAACCC", "AAACTCAAACCC"]
# dna_strings = ["aggtactt", "ccatacgt", "acgttagt", "acgtccat", "ccgtacgg"]
# dna_strings = ["cctgatagacgctatctggctatccacgtacgtaggtcctctgtgcgaatctatgcgtttccaaccat",
#                "agtactggtgtacatttgatacgtacgtacaccggcaacctgaaacaaacgctcagaaccagaagtg",
#                "aaacgtacgtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt",
#                "agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtacgtataca",
#                "ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaacgtacgtc"]
k_value = 3
median = median_string(dna_strings, k_value)
print("Median string:", median)
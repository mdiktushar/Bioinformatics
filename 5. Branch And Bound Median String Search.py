# -*- coding: utf-8 -*-
"""
Created on Sat May 28 14:02:13 2023

@author: MDTus
"""
class Node:
    def __init__(self, motif):
        self.motif = motif
        self.distance = float('inf')
        self.children = []

def hamming_distance(seq1, seq2):
    """Calculate the Hamming distance between two DNA sequences."""
    return sum(nt1 != nt2 for nt1, nt2 in zip(seq1, seq2))

def branch_and_bound_median_string(dna, k):
    """Find the median string motif using branch-and-bound algorithm."""
    best_motif = None
    best_distance = float('inf')
    root = Node('')

    def calculate_distance(motif):
        """Calculate the total distance between a motif and DNA sequences."""
        total_distance = 0
        for seq in dna:
            seq_distance = float('inf')
            for i in range(len(seq) - k + 1):
                substring = seq[i:i+k]
                distance = hamming_distance(motif, substring)
                seq_distance = min(seq_distance, distance)
            total_distance += seq_distance
        return total_distance

    def branch(node):
        nonlocal best_motif, best_distance

        if len(node.motif) == k:
            distance = calculate_distance(node.motif)
            node.distance = distance
            if distance < best_distance:
                best_motif = node.motif
                best_distance = distance
            return

        for nt in 'ACGT':
            child_motif = node.motif + nt
            child_node = Node(child_motif)
            node.children.append(child_node)

        node.children.sort(key=lambda x: calculate_distance(x.motif))
        for child in node.children:
            if calculate_distance(child.motif) < best_distance:
                branch(child)

    branch(root)
    return best_motif

# Example usage
dna_sequences = ['ATGCTAGGCT', 'CTAGGTACGA', 'GCATGCTAGG']
motif_length = 4

result = branch_and_bound_median_string(dna_sequences, motif_length)
print("Best motif found:", result)

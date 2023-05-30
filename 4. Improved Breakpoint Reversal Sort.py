# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:53:49 2023
@author: MDTus

 Implementation only considered inversions as the type of rearrangement. 
 However, genome rearrangement problems can involve various types of 
 rearrangements such as inversions, transpositions, fusions, and fissions. 
 To handle a more general case, a more sophisticated algorithm is required.
"""

def reverse_segment(genome, start, end):
    """Reverses the segment between start and end indices in the genome."""
    segment = genome[start:end + 1]
    reversed_segment = segment[::-1]
    genome[start:end + 1] = reversed_segment
    return genome

def count_breakpoints(genome):
    """Counts the number of breakpoints in the genome."""
    breakpoints = 0
    for i in range(len(genome) - 1):
        if genome[i] + 1 != genome[i + 1]:
            breakpoints += 1
    return breakpoints

def breakpoint_reversal_sort(genome):
    """Performs breakpoint reversal sort on the genome."""
    print("Original genome:", genome)
    breakpoints = count_breakpoints(genome)
    print("Initial breakpoints:", breakpoints)
    step = 1
    
    while breakpoints > 0:
        best_breakpoints = breakpoints
        best_indices = None
        
        for i in range(len(genome) - 1):
            for j in range(i + 1, len(genome)):
                # Reverse the segment between indices i and j
                reversed_genome = reverse_segment(genome[:], i, j)
                
                # Count the breakpoints in the reversed genome
                reversed_breakpoints = count_breakpoints(reversed_genome)
                
                # Check if the reversed genome has fewer breakpoints
                if reversed_breakpoints < best_breakpoints:
                    best_breakpoints = reversed_breakpoints
                    best_indices = (i, j)
        
        # If a better reversal is found, apply it to the genome
        if best_indices is not None:
            start, end = best_indices
            genome = reverse_segment(genome, start, end)
            breakpoints = best_breakpoints
            print("Step", step, "- Reversed segment from index", 
                  start, "to", end)
            print("Current genome:", genome)
            print("Current breakpoints:", breakpoints)
            step += 1
        else:
            break
    
    return genome

# Example usage
genome = [5, 4, 3, 2, 1]

sorted_genome = breakpoint_reversal_sort(genome)
print(sorted_genome)


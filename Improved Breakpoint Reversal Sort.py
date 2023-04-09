def is_sorted(arr):
    """
    Helper function to check if an array is sorted in ascending order.
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def reverse_subarray(arr, start, end):
    """
    Helper function to reverse a subarray within an array.
    """
    arr[start:end + 1] = reversed(arr[start:end + 1])
    return arr


def find_breakpoints(arr):
    """
    Returns a list of indices where breakpoints occur in the array.
    """
    breakpoints = []
    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            breakpoints.append(i + 1)
    return breakpoints



def breakpoint_reversal_sort(arr, max_iterations=1000):
    """
    Sorts an array using the Breakpoint Reversal Sort algorithm.
    """
    iterations = 0
    while not is_sorted(arr):
        breakpoints = find_breakpoints(arr)
        if len(breakpoints) == 0:
            # If there are no breakpoints, the array is already sorted
            break
        elif len(breakpoints) == 1:
            # If there is only one breakpoint, reverse the subarray from the breakpoint to the end
            arr = reverse_subarray(arr, breakpoints[0] - 1, len(arr) - 1)
            iterations += 1
        else:
            # If there are two breakpoints, reverse the subarray between the first two breakpoints
            arr = reverse_subarray(arr, breakpoints[0] - 1, breakpoints[1] - 1)
            iterations += 1
        if iterations >= max_iterations:
            # If the number of iterations exceeds the maximum allowed, terminate to avoid infinite loop
            print("Maximum iterations reached. Terminating to avoid infinite loop.")
            break

    return arr


# Example usage:
# arr = [1, 3, 2, 4, 5]
arr = [5, 4, 3, 2, 1]
print("Original array:", arr)
sorted_arr = breakpoint_reversal_sort(arr, max_iterations=1000000)  # You can adjust the maximum allowed iterations
print("Sorted array:", sorted_arr)

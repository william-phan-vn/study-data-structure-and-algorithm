# Here's a Python implementation of Merge Sort:

def merge(left_half, right_half):
    combined = []
    i = j = 0  # Initialize indices for left and right halves
    # Loop through the left and right halves to merge them by comparing elements
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            combined.append(left_half[i])
            i += 1
        else:
            combined.append(right_half[j])
            j += 1
    
    # Check if any element was left in the left_half or right_half
    while i < len(left_half):
        combined.append(left_half[i])
        i += 1
    
    while j < len(right_half):
        combined.append(right_half[j])
        j += 1

    return combined

# Create a recursive function to divide the array into halves
def merge_sort(arr):
    # Define the base case for the recursive function 
    # to return the array if it has only one element
    if len(arr) == 1:
        return arr
    
    # Divide the array into two halves by finding the middle by floor division. 
    # Ex. [1, 2, 3, 4, 5] -> mid = 2 -> [1, 2] and [3, 4, 5]
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)
    

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", merge_sort(arr))

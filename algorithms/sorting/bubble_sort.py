# Bubble sort is a simple sorting algorithm that repeatedly steps through the list, 
# compares adjacent elements, and swaps them if they are in the wrong order. 
# The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 
# Here's how you can implement bubble sort in Python:

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to indicate whether any swaps were made in this pass
        swapped = False

        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in this pass, the array is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)


# In this code:
# We use a nested loop, where the outer loop iterates through all elements, and the inner loop compares adjacent elements and swaps them if they are in the wrong order.
# We keep track of whether any swaps were made in a pass using the swapped flag. If no swaps were made in a pass, it means the array is already sorted, and we can break out of the outer loop early.
# The inner loop's range is adjusted by n - i - 1 because after each pass, the largest (or smallest, depending on sorting order) element bubbles up to the end of the array, so we don't need to check it again.
# The code continues to perform passes until no swaps are needed, ensuring the list is fully sorted when the algorithm terminates.
# This is a basic example of bubble sort. 
# While it's not the most efficient sorting algorithm for large lists, it's useful for educational purposes and for small lists where simplicity is more important than speed.


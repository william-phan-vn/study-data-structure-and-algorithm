## Problem 1. Finding the Square Root of an Integer
The expected time complexity is O(log(n))

**Solution:** Except the special case (0, 1), compare the half value until found the value whose square is less than or equal to the given number.

## Problem 2. Search in a Rotated Sorted Array
The expected time complexity is O(log(n))

**Solution**
- Find the pivot point by recursively split array in to 2 half
- Use binary search to search the array from the pivot point

## Problem 3. Rearrange Array Elements
The expected time complexity is O(nlog(n))

**Solution**
- Find the number of digits in both the number to satisfy that they cannot differ by more than 1.
- Sort the list using Merge Sort, it takes O(nlog(n)) time
- Take the largest value in the array in turn as the next digit for each number.
  (ex. [1, 2, 3, 4] -> 4 for number A (4_), then 3 for number B(3_), then 2 for number A(42), and then B(31).
This will make sure that we always have the biggest value for larger digit level. This operation takes ~O(n) time.

So the overall time complexity is O(nlog(n))

## Problem 4. Dutch National Flag Problem
Sort the array in a single traversal
--> Count the number of 0, 1, 2. Then transform to the sorted array result

## Problem 5. 
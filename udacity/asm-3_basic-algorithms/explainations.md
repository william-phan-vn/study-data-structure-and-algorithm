## Problem 1. Finding the Square Root of an Integer
The expected time complexity is O(log(n))

**Solution:** Except the special case (0, 1), compare the half value until found the value whose square is less than or equal to the given number.
We don't have list variable so the space complexity is O(1). 

## Problem 2. Search in a Rotated Sorted Array
The expected time complexity is O(log(n))

**Solution**
- Find the pivot point by recursively split array in to 2 half. It takes O(n) space.
- Use binary search to search the array from the pivot point. It takes O(n) space.


## Problem 3. Rearrange Array Elements
The expected time complexity is O(nlog(n))

**Solution**
- Find the number of digits in both the number to satisfy that they cannot differ by more than 1.
- Sort the list using Merge Sort, it takes O(nlog(n)) time and O(n) space.
- Take the largest value in the array in turn as the next digit for each number.
  (ex. [1, 2, 3, 4] -> 4 for number A (4_), then 3 for number B(3_), then 2 for number A(42), and then B(31).
This will make sure that we always have the biggest value for larger digit level. This operation takes ~O(n) time and O(n) space.

So the overall time complexity is O(nlog(n)), and the space complexity is O(n).

## Problem 4. Dutch National Flag Problem
Sort the array in a single traversal
--> Count the number of 0, 1, 2. Then transform to the sorted array result
The time complexity is O(n) and space complexity is O(n)

## Problem 5. Autocomplete with Tries

As the title, we use Trie data structure to resolve the problem.
- For insertion() and finding() operation, we loop through the word/prefix characters, so it takes O(n) time and O(n) space.
- For suffixes() operation, we traverse from the prefix_node collecting all the suffixes, it takes O(n) time and O(nlog(n)) space.
The overall time complexity is O(n) and space complexity is O(nlog(n)).

## Problem 6. Max and Min in a Unsorted Array
The expected time complexity is O(n).
Solution: Traverse the unordered array and find the max and min values.
The space complexity is O(n)

## Problem 7. HTTPRouter using a Trie
We use a Trie like problem 5. But we just find a specific item instead of list down all. 
So it's time complexity is O(n), and space complexity is O(n)

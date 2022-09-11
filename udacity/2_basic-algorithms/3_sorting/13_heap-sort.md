# Heapsort

A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted.  

The main steps in a heapsort are:
1. Convert the array into a maxheap (a complete binary tree with decreasing values) 
2. Swap the top element with the last element in the array (putting it in it's correct final position)
3. Repeat with `arr[:len(arr)-1]` (all but the sorted elements)

## Visualization of a heapsort
![animation of a heap sort](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)

["Heapsort example"](https://commons.wikimedia.org/wiki/File:Heapsort-example.gif) by Swfung8. Used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en).

## Problem statement

In the cell below, see if you can code a `heapsort` function that takes an array (or Python list) and performs a heapsort on it. You will have to complete the heapify
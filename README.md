# Merge-Sort
The Merge Sort algorithm first iteratively divides the array into equal partitions until each partition reduces to a single element. Then it combines them in the same manner as they were divided in an ordered way.
- Divide and Conquer technique
Merge Sort is a recursive technique wherein the unsorted elements are divided into two halves/parts and the function calls itself for the parted halves in a manner such that the halves keep recursively dividing themselves into two parts until the entire array is sorted.

It recursively calls itself for the halves or sub-lists until it gets all the elements separated and that no further division is possible i.e. every sub-list contains 1 (single) element.

Then, the elements are sorted using the basic technique of comparison and swap. 
Finally, it merges all the elements together to get the final sorted list of data items.

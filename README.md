# Merge-Sort
The Merge Sort algorithm first iteratively divides the array into equal partitions until each partition reduces to a single element. Then it combines them in the same manner as they were divided in an ordered way.
### Divide and Conquer technique
- Merge Sort is a recursive technique wherein the unsorted elements are divided into two halves/parts and the function calls itself for the parted halves in a manner such that the halves keep recursively dividing themselves until every element is divided into single segment.

![image](https://user-images.githubusercontent.com/88529671/218426333-e158a817-e662-4d22-81c3-f08b8f9a9276.png)


- It recursively calls itself for the halves or sub-lists until it gets all the elements separated and that no further division is possible i.e. every sub-list contains 1 (single) element.

- Then, the elements are sorted using the basic technique of comparison and swap. 
- Finally, it merges all the elements together to get the final sorted list of data items.

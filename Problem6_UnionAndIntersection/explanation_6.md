# Overview

The goal was to implement `intersection` and `union` methods working on linked lists. I have used a Python `set()` function, that is essentially a hash map that does not store values for given keys. In that sense the item lookup is `O(1)`.

For `union()` method I iterate over all elements in both lists, appending values into a shared set. Set deals does not allow for duplicates entries. Finally, we're looping over each element in the created set appending to a new and empty linked list.

For `intersection()` method. I am creating two `set()`, one for each linked list. Then these sets are converted to a sorted list of elements. To create an intersecting set, I am creating two helper indexes - one for each linked list. I am utilizing the fact that they are sorted:
- if two elements equal at a particular index (initialized to 0), then I am appending this value to the resulting LinkedList. If value from list 1 is smaller, than the value from the list 2, then I am increasing the index corresponding to list 1, and analogically for list 2. The result is a LinkedList containing only a common "intersecting" elements present in both lists.

---
# Time and Space Complexity
- `N1/N2` number of elements in first/second list
- `N` is the sum of `N1+N2`

## Time complexity

### Union
Union time complexity `O(N) = O(N1+N2)`. 

We're looping over each element in list 1, and list 2. In the worst case scenario they have no intersection, so we'll have to repeat `O(N)` when creating the union linked list. All this simplifies to `O(N)`.

### Intersection

Intersection time complexity is `O(N1 logN1 + N2 logN2)`

First, I loop over all elements from two lists in `O(N1+N2)=O(N)`. Then two lists, of `N1` and `N2` elements are sorted, so it takes: `O(N1 logN1 + N2 logN2)`. Final computation iterates in the worst case over all elements from two lists, so it takes `O(N1+N2)`. All the above simplifies finally to `O(N1 logN1 + N2 logN2)`

## Space complexity

### Union

Space complexity of Union is `O(N) == O(N1+N2)`

I am creating one set of size (worst case scenario)`N1+N2 = N`, and then create a linked list of size `N` (worst case). This simplifies to `O(N)=O(N1+N2)`.

### Intersection

Space complexity of Intersection is `O(N)=O(N1+N2)`.

First, I create two sets containing `N=N1+N2` elements. These sets are converted into lists in an "in place" manner (I omit how python handles that with garbage collector). Then the new LinkedList is created which contains in worst case scenario `O(N)` elements, i.e. when `N1==N2` and all elements are shared. Hence, the resulting space complexity is `O(N)`.

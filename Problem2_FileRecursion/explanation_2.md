# Overview
---

The goal is to traverse a file structure, a tree, of unknown depth, and check for each file if it ends with a provided suffix. I've implemented this as a **recursive solution**: starting at the provided "root" directory I am obtaining a list of all files+subdirectories. Files are checked for the presence of a suffix, while the subdirectories are traversed further with a recurrent call to the same function specifying a subdirectory path. The results from all recursive calls are aggregated in the list of files and their paths matching given suffix. 

---
---
---

# Time and Space Complexity

## Time complexity
The algorithm traverses once all elements on the provided folder tree: `n`. For files the amount of operation is constant, as we check only for an existence of the suffix. Hence, the resulting algorithm is `O(n)`.

## Space complexity
The aggregated list of files matching the suffix is proportional to the number of elements in the folder tree. The space complexity of the solution is `O(n)`. 

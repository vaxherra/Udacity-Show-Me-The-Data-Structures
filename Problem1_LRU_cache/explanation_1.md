# Overview
---
## `LRU_cache` implementation

The `LRU_cache` implementation uses a combination of a Hash-Map (Python dictionary `dict()`), to store the key-value pairs, and Nodes of a doubly-linked list to track the order in which the key-value pairs were accessed. 

The dictionary provies a mapping of keys to Nodes of a doubly linked list. The nodes have `next` and `prev` points that point correspondingly to the more and less recently accessed nodes. The nodes also hold themselves a key-value pair.

Whenever a value is set or accessed, apart from the obvious dictionary operations of get and set that take `O(1)` time, the set of `next` and `prev` pointers are manipulated in such a way as to keep track of the order in which the elements were accessed. Number of operations on Nodes of a doubly-linked list are constant, and do not depend on the size of the input. This is due to the fact that access, append and delete operations on the head and tail of the doubly-linked lists are constant `O(1)`.

---
---
---

# Time and space complexity
---
## Time complexity
As discussed above, the time complexity of the implemented `LRU_Cache` is `O(1)` - it is constant, and does not depend on the size of the input.

## Space complexity
The space complexity is `O(n)`, since both hash maps (Python dictionary) and doubly-linked lists scale linearly with the size of the input. 
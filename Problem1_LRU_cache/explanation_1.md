# Overview
---
## `OrderedDict`
The desired building-block structure of the `LRU_cache`, as specified in the task description, asks to implement a structure resembling a Hash-Map. For this purpose however, the Python dictionary (a Hash-Map-like structure) is not sufficient, as elements in hash-map do not maintain order of elements. 

For this reason a Python `OrderedDict` from the `collections` module provides the necessary foundation. This Hash-Map keeps track of the order in which elements were inserted into the collection.

The Python implementation utilizes a Doubly-linked list to efficiently store the order in which elements were inserted into the dictionary: 
https://hg.python.org/cpython/file/2.7/Lib/collections.py

The set and delete operations are performed in constant time `O(1)`, as the Doubly-Linked-List is **never** traversed fully, as the Hash-Map (Python dictionary) keeps track of the elements, next placed in this list.

Hence, the Time complexity of `set` and `get` operations is the same as in standard dictionary. The space complexity is still proportional to the input size `O(n)`, i.e. the same as standard dictionary.

## `LRU_cache` implementation
The implementation of `LRU_cache` becomes straightforward after obtaining the necessary `OrderedDict` instance. 

I make sure the `LRU_capacity` provided to the constructor is at least `1`. 
The **get** operation tries to obtain a `value` for a given `key`. If the key is not present, it returns the `-1`, otherwise it returns the value. Additionally, it moves the recently accessed element to the beginning of the doubly-linked list (`move_to_end` method of OrderedDict).

The **set** operation first tries to remove a given key if it exists. We do this so as to not only overwrite given key value, but to add it to the beginning of our linked-list that tracks the order of our elements.

If the key we want to add to the LRU_cache does not exist, it means we're extending the `LRU_cache` with a new element, and need to check whether we're exceeding its capacity. If we do, then we remove the last item in the `OrderedDict` corresponding to our `Least Recently Used` element. Finally, for every eventuality we add a key-value pair to the `OrderedDict`. 

---
---
---

# Time and space complexity
---
## Time complexity
Time complexity for both get/set method is `O(1)`, as this implementation relies on `OrderedDict`, which in turn intelligently used a `Dictionary` with a doubly-linked list to track items order. 

## Space complexity
Space complexity is `O(n)`, as it effectively uses a python `OrderedDict` - dictionary combined with linked list.
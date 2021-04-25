# Overview

## Node class
First, I've implemented the Abstract Base Class (`ABC`) for a node that holds the frequency of a character. I've implemented the magic methods for comparing instances of this class with respect to the frequency. This proves useful when utilizing heap queue.
Additionally, there is also logic for adding two nodes together. Adding two leaf nodes, or two internal nodes, produces one internal node holding the one with lower frequency on the left, the one with the higher frequency on the right.

The leaf nodes and internal nodes inherit from Node `ABC`. Leaf class holds a character, whereas an internal node holds `left` and `right` elements of a binary tree.

## Huffman encoding

The Huffman encoding starts with building a frequency table of characters in `O(n)`. Then, the list of leaf nodes is created for each entry in this frequency table in `O(n)`. Finally, this list is converted to a Heap Queue in O(n). With Heap Queue, have O(log n) time for insertion and removal [[source](https://en.wikipedia.org/wiki/Priority_queue)]. We're doing it proportionally to the `n` number of characters, giving the `O(n log n)` complexity in the while loop. Finally, using the constructed tree, we construct the codes hash-map by recursively visiting all elements in the tree, this is linearly proportional to the number of elements `O(n)`, and then encoding the input data with these codes takes `O(n)` time. 
This gives the final time complexity of `O(n log n)`.

The space complexity of Huffman Encoding. Storing the frequency of all characters, then the nodes in the Heap Queue, the tree, the codes and encoded data is linearly proportional to the input size: `O(n)`.

[[source: heapq standard Python library](https://docs.python.org/3/library/heapq.html#module-heapq)]. 

## Huffman decoding
The Huffman decoding loops over every bit in the encoded data and traverses the tree generated during Huffman encoding. If the encountered bit is `0` we take the left child of an Internal Node, if the bit is `1` we take the right child of the Internal Node. If the node encountered is a Leaf Node, we extract and append its character to the decoded sequence. 

First, we have to notice that the input are the encoded bits of length `k`. It corresponds to the `n` number of characters in the encoded string. Another take on this complexity is to ackowledge that for each of this character (comprising of multiple bits) we need to traverse the tree for every character. The tree contains `n` symbols, and on average it takes `O(log n)` to decode that symbol, as we don't need to visit all the nodes. So this gives us the final `O(n log n)` time complexity. 

The space complexity is simple here, as we need to store the decoded text which is `O(n)`, where `n` is the original input size to the encoder. 

---
---
---

# Time and Space Complexity
Discussion is provided above. Here I list the final complexities.

## Time Complexity
- Huffman Encoding: `O(n log n)`
- Huffman Decoding: `O(n log n)`

## Space complexity

- Huffman Encoding: `O(n)`
- Huffman Decoding: `O(n)`

## Complexity note

In many cases, time complexity is not very important in the choice of algorithm here, since n here is the number of symbols in the alphabet, which is typically a very small number (compared to the length of the message to be encoded); whereas complexity analysis concerns the behavior when n grows to be very large.
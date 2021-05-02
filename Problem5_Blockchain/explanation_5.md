# Overview

Provided simple implementation of the BlockChain idea utilizes a linked list of BlockChain nodes. 

First, a `Block` of the blockchain is implemented. It holds the data to be stored, the timestamp, and the hash of the previous block, as well as the hash of the current block that is calculated utilizing all the former entries. 

A `Block` is incorporated into a `BlockChainNode` that contains the `next` pointer. It is essentially a node of the singly-linked list.

Finally a `BlockChain` class is implemented. This class holds the beginning of the blockchain `head`, and its end `tail`. The `BlockChain` cannot be altered, and hence only the `append` method is present. This method, given a string of data to be stored in a blockchain, constructs a new `BlockChainNode` and placing it in a linked list of these nodes. The timestamps of creation are stored, as well as hash codes for newly added blocks are calculated.    


# Time and Space complexity
## Time complexity
The input to my simple BlockChain is a string of length `n`. This implementation time complexity is `O(n)`, since the hashing function is linearly proportional to the input string. 

When it comes to a set of connected Blocks, i.e. the BlockChain, accessing the beginning and the end of BlocChain is `O(1)` since we store them in memory. Finding a specific value in a BlockChain of length `m` is `O(m)`, since at worst case scenario, we'd have to traverse each block in the blockchain. 

## Space complexity

For a blockchain of `m` block, each containing `n` characters in the data, the Space complexity is linear, i.e. is proportional to the size of the data, and the number of blocks stored: `O(n*m)`. 

For a single block, it is `O(n)`.
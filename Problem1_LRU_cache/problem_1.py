from collections import OrderedDict
import numpy as np


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        try:
            assert capacity >= 1
            self.capacity = capacity
        except Exception:
            raise ValueError("Capacity must be positive")

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            value = self.cache[key]  # get the value
            self.cache.move_to_end(key)  # the "end" is really our "front", as the most recently used key
            return value
        except KeyError:
            return -1  # in case the key is not there, then we return -1 as requested

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # if the key is there, we have to pop it out of ordered dict, and add it again with a new value
        try:
            self.cache.pop(key)

        except KeyError:  # the key is not present, check for the size, and append a new key to ordered dict
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  # FIFO removal (the oldest one)

        finally:  # append a key-value pair to the ordered dict
            self.cache[key] = value


if __name__ == '__main__':
    
    """Edge case #1, an LRU cache with capacity of 1.
    In such a case we can only store one element
    """
    single_LRU = LRU_Cache(1)
    single_LRU.set(1, 1)
    single_LRU.set(2, 2)

    try:
        assert single_LRU.get(1) == -1
        assert single_LRU.get(2) == 2
        assert single_LRU.get(123) == -1
        single_LRU.set(3, 3)
        assert single_LRU.get(2) == -1
        assert single_LRU.get(3) == 3
    except Exception:
        raise Exception("Case #1 failed")

    print("Case #1 passed")

    """Case #2: big random input to equally big LRU cache
    
    First insert every random int to the LRU cache, as key-value pairs.
    Next set the values to the square of itself. 
    Then make sure each key retrieved from the LRU squared is equal to value.
    
    This makes sure the setting is done correctly. 
    """
    
    random_inputs = np.arange(0, 1e6)  # million integers from 0 to one million-1 ...
    np.random.shuffle(random_inputs)  # ... randomly shuffled

    big_LRU = LRU_Cache(len(random_inputs))

    for random_input in random_inputs:
        big_LRU.set(random_input, random_input)

    for random_input in random_inputs:
        big_LRU.set(random_input, random_input**2)

    for random_input in random_inputs:
        try:
            assert big_LRU.get(random_input) == random_input**2
        except Exception:
            raise Exception("Case #2 test failed for random input")

    print("Case #2 passed")  # prints: case #2 passed

    """Case #3: 
    Creates a thousand of random integers from 0 to 1000. Adds them in order to a LRU cache of size 100. 
    Asserts that only last 100 entries are matching the random inputs, all else have -1 (not present)
    
    """

    random_inputs2 = np.arange(0, 1e3)  # thousand integers from 0 to one million-1 ...
    np.random.shuffle(random_inputs2)  # ... randomly shuffled

    limited_LRU = LRU_Cache(100)

    for random_input2 in random_inputs2:
        limited_LRU.set(random_input2, random_input2)

    for random_input2 in random_inputs2[:-100]:  # all but last one hundred give "-1"
        try:
            assert limited_LRU.get(random_input2) == -1
        except Exception:
            raise Exception("Case #3 failed")

    for random_input2 in random_inputs2[-100:]:
        try:
            assert limited_LRU.get(random_input2) == random_input2
        except Exception:
            raise Exception("Case #3 failed")

    print("Case #3 passed")

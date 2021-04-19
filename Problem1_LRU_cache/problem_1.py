class Node(object):
    """An instance of a node of a doubly-linked list. """

    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val  # (key,value) pair

    def get_key(self):
        return self.val[0]

    def get_val(self):
        return self.val[1]


class LRU_Cache(object):
    """LRU Cache implemented using a Hash Map (python dictionary) and a Doubly Linked List. """

    def __init__(self, capacity):
        self.capacity = capacity  # max capacity of the LRU cache
        self.cache = dict()  # a Hash Map to store the key-valued pairs

        # init head and tail of a doubly linked list
        self.head = None  # the most recently accessed key
        self.tail = None  # the least recently accessed key

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache.keys():
            return -1

        # If the key is the most recently occurring one, return the value, do not change Doubly-Linked List
        if self.cache[key].next is None:
            return self.cache[key].get_val()

        # Here, we need to update the order in which elements are accessed
        if self.cache[key].prev:  # is not None
            self.cache[key].prev.next = self.cache[key].next
        else:  # prev is None, so the given key is at Tail position, update tail
            self.tail = self.cache[key].next

        self.cache[key].next.prev = self.cache[key].prev

        # put the recently access node at the head position
        self.cache[key].prev = self.head
        self.head.next = self.cache[key]
        self.head = self.cache[key]
        self.head.next = None

        return self.cache[key].get_val()

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if self.capacity <= 0 or type(self.capacity) != int:
            print(f"LRU cache capacity is {self.capacity} and cannot hold any information.")
            return

        # If the KEY is in the dictionary, we don't need to worry about LRU_cache capacity, just re-order items
        if key in self.cache.keys():

            # if KEY is already most recently accessed one, replace value and finish
            if self.cache[key].next is None:
                self.cache[key].val = (key, value)
                return

            # Extract the node, and replace its value
            tmp_node = self.cache[key]
            tmp_node.val = (key, value)

            if tmp_node.prev:  # is not None
                tmp_node.prev.next = tmp_node.next
            else:  # tmp_node is a tail
                self.tail = tmp_node.next

            tmp_node.next.prev = tmp_node.prev
            tmp_node.next = None  # most recent node does not have a next Node
            self.head.next = tmp_node  # moves the head
            self.head = tmp_node

            return

        # The key is not present, we need to check capacity: remove least recently used entry first
        if self.capacity == len(self.cache):
            del self.cache[self.tail.get_key()]
            self.tail = self.tail.next

        tmp_node = Node((key, value))

        # If we initialize, we put a value in the hash map and set the head equal to tail tail,
        if len(self.cache) == 0:
            self.head = self.tail = self.cache[key] = tmp_node
            return

        # At this point we know we have space left in the LRU cache, and need to insert it and update the latest node
        # update the most recent entry
        tmp_node.prev = self.head
        self.head.next = tmp_node
        self.head = tmp_node
        # and add it to the HashMap
        self.cache[key] = self.head


if __name__ == "__main__":
    ### Test 1 : LRU cache with capacity of 1
    print("--- Test #1")
    lru = LRU_Cache(1)

    lru.set(1, 1)
    lru.set(10, 10)

    print(lru.get(1))
    # -1
    print(lru.get(10))
    # 10

    ### TEST 2 : LRU without any storage capacity
    print("--- Test #2")
    lru = LRU_Cache(0)

    lru.set(1, 1)
    print(lru.get(1))
    # LRU cache capacity is 0 and cannot hold any information.
    # -1

    ### TEST 3: a simple size-limited LRU cache
    print("--- Test #3")
    lru = LRU_Cache(3)

    for i in range(0, 10):
        lru.set(i, i)

    print(lru.get(2))
    # -1
    print(lru.get(7))
    # 7

    ### TEST 4: access order test
    print("--- TEST 4")
    lru = LRU_Cache(10)

    # set items from 0 to 9
    for i in range(0, 10):
        lru.set(i, i)

    # access items from 9 to 0
    for i in range(9, -1, -1):
        lru.get(i)

    # exceed the LRU capacity by 2 elements
    lru.set(100, 100)
    lru.set(200, 200)

    print(lru.get(9))
    # -1
    print(lru.get(0))
    # 0
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union_hash_map = set()  # set uses a python hashtable (with Values set to Null); gives O(1) membership checks.

    # loop over each element for each list and appendi it to a hashmap
    for llist in [llist_1, llist_2]:
        curr = llist.head
        while curr:
            union_hash_map.add(curr.value)
            curr = curr.next

    # loop over each element in union, creating a joint linked list of common elements
    ll = LinkedList()
    for e in union_hash_map:
        ll.append(e)

    return ll


def intersection(llist_1, llist_2):

    if llist_1.size() == 0 or llist_2.size() == 0:  # intersection with an empty list is empty
        return LinkedList()

    s1, s2 = set(), set()  # placeholders

    # add each element to a set (a special case of a hash map)
    curr = llist_1.head
    while curr:
        s1.add(curr.value)
        curr = curr.next

    curr = llist_2.head
    while curr:
        s2.add(curr.value)
        curr = curr.next

    # sort elements
    s1 = sorted(s1)  # O(n log n)
    s2 = sorted(s2)  # O(n log n)

    idx1 = idx2 = 0
    ll_intersection = LinkedList()

    while idx1 < len(s1) and idx2 < len(s2):
        if s1[idx1] == s2[idx2]:
            ll_intersection.append(s1[idx1])
            idx1 += 1
            idx2 += 1
        elif s1[idx1] < s2[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return ll_intersection


if __name__ == "__main__":
    # Test case 1
    print("Test Case #1")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))  # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21
    print(intersection(linked_list_1, linked_list_2))  # 4 -> 6 -> 21 ->

    # Test case 2
    print("Test Case #2")

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))  # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
    print(intersection(linked_list_3, linked_list_4))  # "" (empty linked list)

    # Test case #3
    print("Test Case #3: intersection of an empty and non-empty list is an empty list:")

    empty = LinkedList()
    nonEmpty = LinkedList()

    [ nonEmpty.append(i) for i in element_1]

    print(intersection(empty,nonEmpty)) # "" (nothing)

    # Test case #4
    print("Test Case #4: union of two identical (element-wise) lists has the same size")

    l1 = LinkedList()
    l2 = LinkedList()
    [ (l1.append(i), l2.append(i)) for i in range(0,5) ]

    print( l1.size()  == intersection(l1,l2).size()  )  # True

    # Test case #5
    print("Test Case #5: Intersection and a union with itself, gives the same set")

    one = LinkedList()
    [one.append(i) for i in range(0,200)]

    print(intersection(one,one).size() == union(one,one).size())  # True

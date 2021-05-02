import hashlib
from datetime import datetime


class Block:
    """A Blockchain block. Containing data, a timestamp of creation, and a previous block hash.
    A `calc_hash` function calculates the current block's hash code, taking into account current data,
    timestamp and previous block hash.
    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        # new hash is created using current block data and timestamp, as well as previous block hash
        if self.previous_hash:
            hash_str = (str(self.data) + str(self.previous_hash) + str(self.timestamp)).encode('utf-8')
        else:  # if previous hash is None, do not use it to construct current hash string
            hash_str = (str(self.data) + str(self.timestamp)).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def __repr__(self):
        data = {'data': self.data,
                'timestamp': self.timestamp,
                'previous_hash': self.previous_hash, 
                'hash': self.hash}

        data = "{" + '\n'.join([str(k) + ":" + str(v) for k, v in data.items()]) + "}"

        return str(data)


class BlockChainNode(object):
    """A BlockChain Node. Is a container storing a BlockChain 'block', as well as a pointer to the next block.
    """

    def __init__(self, data, prev_node):
        if prev_node:  # if previous block occurs (is not None)
            prev_hash = prev_node.block.get_hash()
        else:  # no previous block - the beginning of a BlockChain
            prev_hash = None
        self.block = Block(timestamp=datetime.utcnow(), data=data, previous_hash=prev_hash)
        self.next = None

    def __repr__(self):
        return str(self.block)


class BlockChain(object):
    """A BlockChain is a set of connected BlockChain Nodes. It contains the beginning of the blockchain, as well as
    the most recent block (tail).

    It contains only the append method, to append a new data entry in the form of a string. This append method
    creates a BlockChain block, and a BlockChain node and connects them appropriately."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if data is None:
            raise ValueError("Data cannot be None")

        if self.head:  # if head is present
            self.tail.next = BlockChainNode(data=data, prev_node=self.tail)
            self.tail = self.tail.next

        else:  # head is empty
            self.head = self.tail = BlockChainNode(data=data, prev_node=None)

    def __repr__(self):

        curr = self.head
        return_string = ""

        while curr:
            return_string += str(curr)
            return_string += "\n" + 20*" " + "|"
            return_string += "\n" + 20*" " + "V" + "\n"
            curr = curr.next

        return return_string


if __name__ == "__main__":
    print("Test #1: A small blockchain")

    myBlockChain = BlockChain()

    for i in range(1, 4):
        myBlockChain.append(f"Entry #{i}")

    print(myBlockChain)
    """
    {data:Entry #1
    timestamp:2021-05-02 10:31:31.673030
    previous_hash:None
    hash:5414dc326398fe5497cb107ee5d05f825d8d94d48d59199dbb93b1ce6810cb3b}
                        |
                        V
    {data:Entry #2
    timestamp:2021-05-02 10:31:31.673300
    previous_hash:5414dc326398fe5497cb107ee5d05f825d8d94d48d59199dbb93b1ce6810cb3b
    hash:73b2f7c2fe4c9b4888a7bba62c0c31febc7185ffdbf5483cf4cac5e877639b1c}
                        |
                        V
    {data:Entry #3
    timestamp:2021-05-02 10:31:31.673312
    previous_hash:73b2f7c2fe4c9b4888a7bba62c0c31febc7185ffdbf5483cf4cac5e877639b1c
    hash:571cd839aa98d68d9b4c993d6af9646221708b9f0812a76594ae82a0add74987}
                        |
                        V
    """

    print("Test #2: Empty BlockChain")

    myBlockChain = BlockChain()
    print(myBlockChain)  # empty new line ""

    print("Test #3: BlockChain with the exact same data")

    myBlockChain = BlockChain()

    for _ in range(1, 4):
        myBlockChain.append(data="Same data")

    print(myBlockChain)  # blockchain contains the same data, but the hash values, and timestamps are different
    """
    {data:Same data
    timestamp:2021-05-02 10:31:31.673379
    previous_hash:None
    hash:17613de095d44ce5e06c3bea607f0901d9f3cfca8432fb367b4029304a2349be}
                        |
                        V
    {data:Same data
    timestamp:2021-05-02 10:31:31.673389
    previous_hash:17613de095d44ce5e06c3bea607f0901d9f3cfca8432fb367b4029304a2349be
    hash:9d11a0f5785a48bcf4125868a6d4c1cf265d3e9f496349e2b797c504111e235d}
                        |
                        V
    {data:Same data
    timestamp:2021-05-02 10:31:31.673396
    previous_hash:9d11a0f5785a48bcf4125868a6d4c1cf265d3e9f496349e2b797c504111e235d
    hash:beb754532802dcf62775a33d0deee740f26c730a792b7c31a38751b5b295d805}
                        |
                        V
    """

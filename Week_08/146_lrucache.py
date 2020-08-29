from collections import OrderedDict
# 使用OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        value = self[key]
        self.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)
        if len(self) > self.capacity:
            self.popitem(last=False)






# 使用hash表和双端链表
class DLinkNode():
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache1:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = DLinkNode(key, value)
            self.size += 1
            self.addToHead(self.cache[key])
            if self.size > self.capacity:
                # self.removeTail()
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

    def moveToHead(self, node):
        node = self.removeNode(node)
        self.addToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
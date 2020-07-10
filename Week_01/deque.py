from typing import List
class Deque:
    def __init__(self):
        self.data :List[int] = []
        self._capacity = 1024
        self._len = 0

    def addfirst(self,k):
        self.data = self.data.insert(0,k)

    def addlast(self,k):
        self.data.append(k)

    def poplast(self):
        return self.data.pop()

    def popfirst(self):
        x = self.data[0]
        self.data = self.data
        return x

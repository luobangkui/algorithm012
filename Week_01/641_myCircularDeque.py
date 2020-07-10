
# 第一遍做，没有在原数组上进行操作，看过大佬的答案之后，发现搞错了
# 注意点是双端队列需要使用front和rear 双指针，插入和删除需要模%的操作


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.data = [-1] * k
        self.capality = k
        self.front ,self.rear = 0 ,0
        self.size = 0


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[self.front] = value
        else:
            self.front = (self.front -1 ) %self.capality
            self.data[self.front] = value
        self.size += 1
        return True



    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[self.rear] = value
        else:
            self.rear = (self.rear +1 ) %self.capality
            self.data[self.rear] = value
        self.size += 1
        return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.data[self.front] = -1
        self.front = (self.front +1 ) %self.capality
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.data[self.rear] = -1
        self.rear = (self.rear -1 ) %self.capality
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]



    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capality
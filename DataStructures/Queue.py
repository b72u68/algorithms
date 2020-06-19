class Queue:

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, val):
        if not self.head:
            self.head = self.tail = Queue.Node(val)
        else:
            self.tail.next = self.tail = Queue.Node(val)

    def dequeue(self):
        assert self.head
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def empty(self):
        return self.head == None

class LinkedList:

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def prepend(self, value):
        self.head = LinkedList.Node(value, next=self.head)

        if not self.tail:
            self.tail = self.head

        self.count += 1

    def append(self, value):
        if len(self) == 0:
            self.prepend(value)
        else:
            self.tail.next = LinkedList.Node(value, next=None)
            self.tail = self.tail.next

            self.count += 1

    def del_head(self):
        assert(len(self) > 0)

        if self.head:
            self.head = self.head.next
            self.count -= 1
        
        if len(self) == 0:
            self.tail = None

    def del_tail(self):
        assert(len(self) > 0)

        if len(self) == 1:
            self.head = self.tail = None
        else:
            n = self.head
            while n.next.next:
                n = n.next

            n.next = None
            self.tail = n
            self.count -= 1

    def __len__(self):
        return self.count 

    def __iter__(self):
        n = self.head
        while n:
            yield n.val
            n = n.next

    def __repr__(self):
        return '[' + ', '.join(str(x) for x in self) + ']'

class LinkedList:
    
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.count = 0

    def prepend(self, value):
        self.head = LinkedList.Node(value, next=self.head)
        self.count += 1

    def append(self, value):
        if len(self) == 0:
            self.prepend(value)
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = LinkedList.Node(value, next=None)
            self.count += 1

    def del_head(self):
        assert(len(self) > 0)
        
        if self.head:
            self.head = self.head.next
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

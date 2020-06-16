class LinkedList:

    class Node:
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next = next

    def __init__(self):
        self.head = LinkedList.Node(None)
        self.head.prior = self.head
        self.head.next = self.head
        self.count = 0

    def prepend(self, value):
        n = LinkedList.Node(value, prior=self.head, next=self.head.next)
        self.head.next = n
        self.head.next.prior = n
        self.count += 1

    def append(self, value):
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        self.head.prior.next = n
        self.head.prior = n
        self.count += 1

    def __getitem__(self, idx):
        assert(idx < len(self))

        n = self.head.next
        for _ in range(idx):
            n = n.next

        return n.val

    def del_head(self):
        assert(len(self) > 0)

        to_del = self.head.next
        to_del.prior.next = to_del.next
        to_del.next.prior = to_del.prior
        self.count -= 1

    def del_tail(self):
        assert(len(self) > 0)

        to_del = self.head.prior
        to_del.prior.next = to_del.next
        to_del.next.prior = to_del.prior
        self.count -= 1

    def __len__(self):
        return self.count

    def __iter__(self):
        n = self.head.next
        while n is not self.head:
            yield n.val
            n = n.next

    def __repr__(self):
        return '[' + ', '.join(str(x) for x in self) + ' ]'

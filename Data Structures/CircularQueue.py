class Queue:

    def __init__(self, limit=10):
        self.data = [None]*limit
        self.head = -1
        self.tail = -1

    def enqueue(self, val):
        if (self.tail + 1) % len(self.data) == self.head:
            raise RuntimeError
        else:
            if self.head == -1:
                self.head = self.tail = 0
            else:
                self.tail = (self.tail + 1) % len(self.data)
            self.data[self.tail] = val

    def dequeue(self):
        if self.tail == -1:
            raise RuntimeError
        else:
            data = self.data[self.head]
            self.data[self.head] = None
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % len(self.data)
            return data

    def resize(self, newsize):
        assert(len(self.data) < newsize)
        q = []
        for val in self:
            q.append(val)
        self.tail = len(q) - 1
        for _ in range(newsize - len(self.data)):
            q.append(None)
        self.data = q
        self.head = 0 

    def empty(self):
        for val in self.data:
            if val is not None:
                return False
        return True

    def __bool__(self):
        return not self.empty()

    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)

    def __iter__(self):
        idx = self.head
        if self.head >= self.tail:
            for _ in range(len(self.data)-(self.head-self.tail)+1):
                yield self.data[idx % len(self.data)]
                idx += 1
        else:
            for i in range(self.head, self.tail + 1):
                yield self.data[i]

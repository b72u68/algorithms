class Heap:
    
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key = key

    @staticmethod
    def _parent(idx):
        return (idx-1)//2

    @staticmethod
    def _left(idx):
        return idx*2+1

    @staticmethod
    def _right(idx):
        return idx*2+2

    def _heapify(self, idx=0):
        while True:
            l = Heap._left(idx)
            r = Heap._right(idx)
            maxidx = idx

            if l < len(self) and self.key(self.data[l]) > self.key(self.data[idx]):
                maxidx = l
            if r < len(self) and self.key(self.data[r]) > self.key(self.data[maxidx]):
                maxidx = r

            if maxidx != idx:
                self.data[idx], self.data[maxidx] = self.data[maxidx], self.data[idx]
                idx = maxidx
            else:
                break

    def _heapify_rec(self, idx=0):
        l = Heap._left(idx)
        r = Heap._right(idx)
        maxidx = idx

        if l < len(self) and self.key(self.data[l]) > self.key(self.data[idx]):
            maxidx = l
        if r < len(self) and self.key(self.data[r]) > self.key(self.data[maxidx]):
            maxidx = r
        if maxidx != idx:
            self.data[idx], self.data[maxidx] = self.data[maxidx], self.data[idx]
            self._heapify_rec(maxidx)

    def add(self, val):
        self.data.append(val)

        i = len(self.data) - 1
        p = Heap._parent(i)

        while i > 0 and self.key(self.data[i]) > self.key(self.data[p]):
            self.data[i], self.data[p] = self.data[p], self.data[i]
            i = p
            p = Heap._parent(i)

    def peek(self):
        return self.data[0]

    def pop(self):
        ret = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        self._heapify()
        return ret

    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)

class ArrayList:

    def __init__(self):
        self.data = []

    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self.data)
            if nidx < 0:
                nidx = 0
        return nidx

    def append(self, value):
        self.data.append(value)

    def __getitem__(self, idx):
        assert(isinstance(idx, int))
        idx = self._normalize_idx(idx)
        if idx >= len(self.data):
            raise IndexError
        return self.data[idx]

    def __setitem__(self, idx, value):
        assert(isinstance(idx, int))
        idx = self._normalize_idx(idx)
        if idx >= len(self.data):
            raise IndexError
        self.data[idx] = value

    def __delitem__(self, idx):
        assert(isinstance(idx, int))
        idx = self._normalize_idx(idx)
        if idx >= len(self.data):
            raise IndexError
        for i in range(idx, len(self.data)-1):
            self.data[i] = self.data[i+1]
        del self.data[len(self.data)-1]

    def __len__(self):
        return len(len(self.data))

    def __repr__(self):
        return str(self.data)

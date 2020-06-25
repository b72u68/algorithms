class ArrayList:

    def __init__(self):
        self.data = []

    ### subscipt-based access ###

    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self.data)
            if nidx < 0:
                nidx = 0
        return nidx

    def __getitem__(self, idx):
        """Implements 'x = self[idx]'"""
        assert(isinstance(idx, int))
        idx = self._normalize_idx(idx)
        if idx >= len(self.data):
            raise IndexError
        return self.data[idx]

    def __setitem__(self, idx, value):
        """Implements 'self[idx] = value'"""
        assert(isinstance(idx, int))
        idx = self._normalize_idx(idx)
        if idx >= len(self.data):
            raise IndexError
        self.data[idx] = value

    def __delitem__(self, idx):
        """Implements 'del self[idx]'"""
        assert(isinstance(idx, int))
        idx = self._normalize_idx(idx)
        if idx >= len(self.data):
            raise IndexError
        for i in range(idx, len(self.data)-1):
            self.data[i] = self.data[i+1]
        del self.data[len(self.data)-1]

    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i]

    def __len__(self):
        return len(len(self.data))

    ### stringification ###

    def __str__(self):
        """Implements 'str(self)'. Returns '[]' if the list is empty"""
        if len(self.data) == 0:
            return '[]'
        return '[' + ', '.join(str(x) for x in self.data) + ' ]'

    def __repr__(self):
        return str(self.data)

    ### single-element manipulation ###
    
    def append(self, value):
        """Appends value to the end of this list"""
        self.data.append(None)
        self.data[len(self.data)-1] = value

    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the list"""
        assert(isinstance(idx, int))

        idx = self._normalize_idx(idx)

        if idx > len(self):
            raise IndexError

        self.data.append(None)
        if idx == len(self.data):
            self.data[len(self.data)-1] = value
        else:
            for i in range(len(self.data)-1, idx, -1):
                self.data[i] = self.data[i-1]
            self.data[idx] = value

    def pop(self, idx=-1):
        """Deletes and returns the element at idx"""
        assert(isinstance(idx, int))
        
        idx = self._normalize_idx(idx)
        if idx >= len(self):
            raise IndexError
        else:
            pop_val = self[idx]
            del self[idx]
            return pop_val

    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the list"""
        idx = -1

        for i in range(len(self.data)):
            if self.data[i] == value:
                idx = i
                break

        if idx < 0:
            raise ValueError
        else:
            del self[idx]

    ### predicates (T/F queries) ###

    def __eq__(self, other):
        """Returns True if this ArrayList contains the same elements (in order) as other"""
        if type(other) is not ArrayList:
            return False
        else:
            if len(self.data) != len(other):
                return False
            for i in range(len(self.data)):
                if self[i] != other[i]:
                    return False
        return True

    def __contains__(self, value):
        """Implements 'val in self'. Returns True if value is found in this list"""
        for i in range(len(self.data)):
            if self.data[i] == value:
                return True
        return False

    ### queries ###
    
    def min(self):
        """Returns the minimum value of the list"""
        min = self.data[0]
        for i in range(len(self.data)):
            if self.data[i] < min:
                min = self.data[i]
        return min

    def max(self):
        """Returns the maximum value of the list"""
        max = self.data[0]
        for i in range(len(self.data)):
            if self.data[i] > max:
                max = self.data[i]
        return max

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encounted in this list between index i (inclusive) and j (exclusive)"""
        if not j:
            j = len(self.data)

        i, j = self._normalize_idx(i), self._normalize_idx(j)

        if i >= len(self.data) or j > len(self.data):
            raise IndexError

        for idx in range(i, j):
            if self.data[idx] == value:
                return idx

        raise ValueError
        
    def count(self, value):
        """Returns the number of times value appears in the list"""
        counter = 0
        for i in range(len(self.data)):
            if self.data[i] == value:
                counter += 1
        return counter

    ### bulk operations ###

    def __add__(self, other):
        """Implements 'self + other'. Return a new ArrayList instance that contains the values in this list followed by those from other"""
        added = ArrayList()
        for i in range(len(self.data)):
            added.append(self.data[i])
        for i in range(len(other)):
            added.append(self.data[i])
        return added

    def clear(self):
        """Removes all values in this list"""
        self.data = []

    def copy(self):
        """Returns a new ArrayList instance that contains the values of this list"""
        other = ArrayList()
        for i in range(len(self.data)):
            other.append(self.data[i])
        return other

    def extend(self, other):
        """Adds all elements, in order, from other - an Iterable - to this list"""
        it = iter(other)
        for val in it:
            self.data.append(None)
            self.data[len(self.data)-1] = val

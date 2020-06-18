class OrderedHashtable:

    class Node:
        def __init__(self, index, next=None):
            self.index = index
            self.next = next

    def __init__(self, n_buckets=1000):
        self.indices = [None] * n_buckets
        self.entries = []
        self.count = 0

    def __setitem__(self, key, val):
        indices_idx = hash(key) % len(self.indices)
        n = self.indices[indices_idx]

        while n:
            if self.entries[n.index][0] == key:
                self.entries[n.index][1] = val
                return
            n = n.next

        else:
            self.entries.append([key,val])
            self.indices[indices_idx] = OrderedHashtable.Node(len(self.entries)-1, next=self.indices[indices_idx])
            self.count += 1

    def __getitem__(self, key):
        indices_idx = hash(key) % len(self.indices)
        n = self.indices[indices_idx]

        while n:
            if self.entries[n.index][0] == key:
                return self.entries[n.index][1]
            n = n.next

        else:
            raise KeyError

    def __delitem__(self, key):
        del_idx = -1

        indices_idx = hash(key) % len(self.indices)
        n = self.indices[indices_idx]

        while n:
            if self.entries[n.index][0] == key:
                del_idx = self.entries[n.index][1]
                break
            n = n.next

        if del_idx < 0:
            raise KeyError
        else:
            n = self.indices[indices_idx]

            if n.index == del_idx:
                self.indices[indices_idx] = n.next
            else:
                while n.next:
                    if n.next.index == del_idx:
                        break
                    n = n.next

                if n.next.next:
                    n.next = n.next.next
                else:
                    n.next = None

            for i in range(del_idx+1, len(self.entries)):
                key = self.entries[i][0]
                idx = hash(key) % len(self.indices)
                b = self.indices[idx]
                while b:
                    if self.entries[b.index][0] == key:
                        b.index = i - 1
                        break
                    b = b.next

            del self.entries[del_idx]
            self.count -= 1

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

        # indices_idx = hash(key) % len(self.indices)
        # n = self.indices[indices_idx]

        # while n:
            # if self.entries[n.index][0] == key:
                # return True
            # n = n.next

        # return False

    def __len__(self):
        return self.count

    def __iter__(self):
        for i in range(len(self.entries)):
            yield self.entries[i][0]

    def keys(self):
        return iter(self)

    def values(self):
        for i in range(len(self.entries)):
            yield self.entries[i][1]

    def items(self):
        for i in range(len(self.entries)):
            yield tuple(self.entries[i]) 

    def __str__(self):
        return '{' + ', '.join(str(k) + ': ' + str(v) for k,v in self.items()) + ' }'

    def __repr__(self):
        return str(self)

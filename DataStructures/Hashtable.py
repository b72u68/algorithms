class Hashtable:
    
    class Node:
        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self, n_buckets=1000):
        self.buckets = [None] * n_buckets

    def __setitem__(self, key, val):
        bucket_idx = key % len(self.buckets)
        b = self.buckets[bucket_idx]
        while b:
            if b.key == key:
                b.val = val
                return
            b = b.next
        else:
            self.buckets[bucket_idx] = Hashtable.Node(key, val, next=None)

    def __getitem__(self, key):
        bucket_idx = key % len(self.buckets)
        b = self.buckets[bucket_idx]
        while b:
            if b.key == key:
                return b.val
            b = b.next 
        else:
            raise KeyError()

    def __contains__(self, key):
        bucket_idx = key % len(self.buckets)
        b = self.buckets[bucket_idx]
        while b:
            if b.key == key:
                return True
            b = b.next
        else:
            return False

    def __iter__(self):
        for b in self.buckets:
            while b:
                yield b.key
                b = b.next

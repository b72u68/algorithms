class BSTree:

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.size = 0

    def __contains__(self, val):
        def contains_rec(node, val):
            if not node:
                return False
            elif val < node.val:
                return contains_rec(node.left, val)
            elif val > node.val:
                return contains_rec(node.right, val)
            else:
                return True
        return contains_rec(self.root, val)

    def add(self, val):
        assert (val not in self)
        def add_rec(node):
            if not node:
                return BSTree.Node(val)
            elif val < node.val:
                return BSTree.Node(node.val, left=add_rec(node.left), right=node.right)
            else:
                return BSTree.Node(node.val, left=node.left, right=add_rec(node.right))
        self.root = add_rec(self.root)
        self.size += 1

    def __delitem__(self, val):
        assert (val in self)
        def delitem_rec(node):
            if val < node.val:
                node.left = delitem_rec(node.left)
                return node
            elif val > node.val:
                node.right = delitem_rec(node.right)
                return node
            else:
                if not node.left and not node.right:
                    return None
                elif node.left and not node.right:
                    return node.left
                elif node.right and not node.left:
                    return node.right
                else:
                    t = node.left
                    if not t.right:
                        node.val = t.val
                        node.left = t.left 
                    else:
                        n = t
                        while n.right.right:
                            n = n.right
                        t = n.right
                        n.right = t.left
                        node.val = t.val
                    return node

        self.root = delitem_rec(self.root)
        self.size -= 1

    def __iter__(self):
        nodes = [self.root]
        while nodes:
            n = nodes.pop(0)
            yield n.val
            if n.left:
                nodes.append(n.left)
            if n.right:
                nodes.append(n.right)

    def __len__(self):
        return self.size

    def height(self):
        def height_rec(node):
            if not node:
                return 0
            else:
                return max(1+height_rec(node.left), 1+height_rec(node.right))
        return height_rec(self.root)

    def count_less_than(self, val):
        def count_rec(node):
            if not node:
                return 0
            else:
                if node.val >= val:
                    return count_rec(node.left) + count_rec(node.right)
                else:
                    return 1 + count_rec(node.left) + count_rec(node.right)
        return count_rec(self.root)

    def successor(self, x):
        def succ_rec(node, val):
            if not node:
                return None
            else:
                if x == node.val:
                    if node.right:
                        return node.right.val
                    else:
                        return val
                elif x > node.val:
                    return succ_rec(node.right, val)
                else:
                    if node.left:
                        return succ_rec(node.left, node.val)
                    else:
                        return node.val
        return succ_rec(self.root, None)

    def descendants(self, val):
        def des_rec(node):
            if not node:
                return []
            elif val < node.val:
                return des_rec(node.left)
            elif val > node.val:
                return des_rec(node.right)
            else:
                return iter_rec(node.left) + iter_rec(node.right) 

        def iter_rec(node, lst=[]):
            if node:
                iter_rec(node.left, lst)
                lst.append(node.val)
                iter_rec(node.right, lst)
            return lst

        return des_rec(self.root)

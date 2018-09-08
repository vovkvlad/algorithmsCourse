# The same as weighted quick Union, but after calculating root of p,
# set the id  of each examined node to point to that root

# Two-pass implementation: add second loop to root() to set the id[] of each examined node to root
# One-pass implementation: make every other node in path to point to it's grandparent (thereby having path length)

class QuickUnionPathCompression:
    def __init__(self, N):
        self.id = []
        self.sz = []
        for item in range(N):
            self.id.append(item)
            self.sz.append(1)

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j: return

        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

    def print_self(self):
        for index, item in enumerate(self.id):
            print(f'Index: {index} \t Value: {item} \t Size: {self.sz[index]}')
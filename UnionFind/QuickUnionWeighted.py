# Weighted quick union
# - modify quick union to avoid tall trees
# - keep track of tree size (number of objects)
# - Balance by linking smaller tree to root of bigger tree

# Data structure: same quick union but maintain extra array sz[i] to count number of objects in tree rooted at i
# Find: the same as quick union
# Union: 1 - Link smaller tree to larger tree; 2 - update sz array


class QuickUnionWeighted:
    def __init__(self, N):
        self.id = []
        self.sz = []
        for item in range(N):
            self.id.append(item)
            self.sz.append(1)

    def root(self, i):
        while i != self.id[i]:
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

# Running time:
# - Find: takes time proportional to depth of p and q
# - Union: takes constant time, given roots

# Proposition: Depth of any x is at most lg N (base-2 logarithm)
# Proof: When does depth of x increase? It increase by 1 when tree T1 containing x is merged into another tree T2
# - the size of tree containing x at least doubles since |T2| >= |T1|
# - size of tree containing x can double only lg N times
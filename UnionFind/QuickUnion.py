# Data structure:
# integer array of size N
# Interpretation: id[i] is a parent of i
# Root of i is id[id[id....id[i]...]]] - keep going until it doesn't change
# Example: index: 0 1 2 3 4 5 6 7 8 9
#          value: 0 1 9 4 9 6 6 7 8 9
#
#   0 1 9   6 7 8
#      / \  |
#     2   4 5
#         |
#         3
#
# Find - check whether p and q has the same root


class QuickUnion:
    def __init__(self, N):
        self.id = []
        for item in range(N):
            self.id.append(item)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        self.id[i] = j

    def print_self(self):
        for index, item in enumerate(self.id):
            print(f'Index: {index} \t Value: {item}')
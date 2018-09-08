#from UnionFind.QuickFind import QuickFindUf
# from UnionFind.QuickUnion import QuickUnion
from UnionFind.QuickUnionWeighted import QuickUnionWeighted

#quickUF = QuickFindUf(10)

# ============= QuickUnion ==================
#quickUnion = QuickUnion(10)
#quickUnion.print_self()
# print('===================')
# quickUnion.union(2, 4)
# quickUnion.union(4, 6)
# quickUnion.union(6, 9)
# quickUnion.union(3, 7)
# quickUnion.union(7, 6)
# quickUnion.print_self()
# print(f'Root of 2 is {quickUnion.root(2)}')
# print(f'7 and 2 is connected: {quickUnion.connected(2, 7)}')


# ============= QuickUnionWeighted ==================
quickUnionWeighted = QuickUnionWeighted(10)
quickUnionWeighted.print_self()
print('===================')
quickUnionWeighted.union(2, 4)
quickUnionWeighted.union(4, 6)
quickUnionWeighted.union(6, 9)
quickUnionWeighted.union(3, 7)
quickUnionWeighted.union(7, 6)
quickUnionWeighted.print_self()
print(f'Root of 2 is {quickUnionWeighted.root(2)}')
print(f'7 and 2 is connected: {quickUnionWeighted.connected(2, 7)}')
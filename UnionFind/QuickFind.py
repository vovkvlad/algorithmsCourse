class QuickFindUf:
    def __init__(self, N):
        self.id = []
        for i in range(N):
            self.id.append(i)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pId = self.id[p]
        qId = self.id[q]

        for index, item in enumerate(self.id):
            if item == pId:
                self.id[index] = qId

    def print_self (self):
        for index, item in enumerate(self.id):
            print(f'Index: {index} \t Value: {item}')

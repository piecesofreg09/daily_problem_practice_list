class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
    def find(self, x): # log(n)
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y): # log(n)
        root_x = self.find(x)
        root_y = self.find(y)

        rank_x = self.rank[x]
        rank_y = self.rank[y]
        if root_x == root_y:
            return

        if rank_x > rank_y:
            self.root[root_y] = root_x
        elif rank_x < rank_y:
            self.root[root_x] = root_y
        else:
            self.root[root_x] = root_y
            self.rank[root_y] += 1
    
    def connected(self, x, y): # log(n)
        return self.find(x) == self.find(y)

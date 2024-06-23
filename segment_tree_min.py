import math
inf = float('inf')
class MinRange:
    def __init__(self, arr):
        n = len(arr)
        height = int(math.ceil(math.log2(n)))
        total = 2 * (2 ** height) - 1
        print(total)
        self.arr = arr
        self.tree = [inf for i in range(total)]

    def build_util(self, start, end, parent_index):
        if start == end:
            self.tree[parent_index] = self.arr[start]
            return self.arr[start]
        mid = (start + end) // 2

        min_left = self.build_util(start, mid, parent_index * 2 + 1)
        min_right = self.build_util(mid+1, end, parent_index * 2 + 2)

        this_min = min(min_left, min_right)
        self.tree[parent_index] = this_min

        return this_min

    def build(self):
        self.build_util(0, len(arr) - 1, 0)
    
    def query(self, i, j, ri, rj, node_index):
        if i > rj or j < ri:
            return inf
        # reaching the desired boundary
        if i == ri and j == rj:
            print('directly in range', i, j, ri, rj)
            return self.tree[node_index]
        
        mid = (ri + rj) // 2
        if i > mid:
            return self.query(i, j, mid + 1, rj, node_index * 2 + 2)
        elif j <= mid:
            return self.query(i, j, ri, mid, node_index * 2 + 1)
        
        left_query = self.query(i, mid, ri, mid, node_index * 2 + 1)
        right_query = self.query(mid + 1, j, mid + 1, rj, node_index * 2 + 2)

        return min(left_query, right_query)
        
arr = [10,13,12,14,15,17,16,23,1,45,4]
rq = MinRange(arr)
rq.build()
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        print(arr[i:j+1], rq.query(i, j, 0, len(arr) - 1, 0), min(arr[i:j+1]))

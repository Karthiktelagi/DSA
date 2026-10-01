class Node:
    def __init__(self, k: int):
        self.prod = 1
        self.remain = [0] * k

class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        self.k_val = k
        self.tree = [Node(k) for _ in range(4 * n)]
        
        def merge(left: Node, right: Node) -> Node:
            res = Node(self.k_val)
            res.prod = (left.prod * right.prod) % self.k_val
            
            # Left counts stay mapping to the exact same remainders
            for i in range(self.k_val):
                res.remain[i] = left.remain[i]
                
            # Right counts are shifted by multiplying with the total product of the left child
            for j in range(self.k_val):
                if right.remain[j] > 0:
                    target_rem = (left.prod * j) % self.k_val
                    res.remain[target_rem] += right.remain[j]
            return res

        def build(cur: int, left: int, right: int):
            if left == right:
                rem = nums[left] % self.k_val
                self.tree[cur].remain[rem] = 1
                self.tree[cur].prod = rem
                return
            mid = left + (right - left) // 2
            build(2 * cur + 1, left, mid)
            build(2 * cur + 2, mid + 1, right)
            self.tree[cur] = merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])

        def update(cur: int, left: int, right: int, idx: int, val: int):
            if left == right:
                self.tree[cur].remain = [0] * self.k_val
                rem = val % self.k_val
                self.tree[cur].remain[rem] = 1
                self.tree[cur].prod = rem
                return
            mid = left + (right - left) // 2
            if idx <= mid:
                update(2 * cur + 1, left, mid, idx, val)
            else:
                update(2 * cur + 2, mid + 1, right, idx, val)
            self.tree[cur] = merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])

        def query(cur: int, left: int, right: int, ql: int, qr: int) -> Node:
            if ql <= left and right <= qr:
                return self.tree[cur]
            mid = left + (right - left) // 2
            if qr <= mid:
                return query(2 * cur + 1, left, mid, ql, qr)
            if ql > mid:
                return query(2 * cur + 2, mid + 1, right, ql, qr)
            
            return merge(
                query(2 * cur + 1, left, mid, ql, mid),
                query(2 * cur + 2, mid + 1, right, mid + 1, qr)
            )

        # Initial segment tree setup
        build(0, 0, n - 1)
        
        ans = []
        for index_i, value_i, start_i, x_i in queries:
            # 1. Apply the persistent point update 
            update(0, 0, n - 1, index_i, value_i)
            
            # 2. Query the non-empty suffix space starting from start_i to n-1
            ans_node = query(0, 0, n - 1, start_i, n - 1)
            
            # 3. Pull the calculated occurrences of remainder x_i
            ans.append(ans_node.remain[x_i])
            
        return ans

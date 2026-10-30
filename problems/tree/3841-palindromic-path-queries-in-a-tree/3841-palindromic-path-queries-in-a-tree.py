
from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS: Euler entry/exit times and parents
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[u][0] = u if p == -1 else p

                for j in range(1, LOG):
                    parent[u][j] = parent[parent[u][j - 1]][j - 1]

                stack.append((u, p, 1))
                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff >> j & 1:
                    u = parent[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]

            return parent[u][0]

        # Fenwick tree supporting range XOR updates and point queries
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def range_xor(left, right, val):
            add(left, val)
            if right + 1 < n:
                add(right + 1, val)

        def point_query(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def mask(ch):
            return 1 << (ord(ch) - ord('a'))

        chars = list(s)
        base = [0] * n

        # Root-to-node prefix XOR masks
        stack = [(0, -1, 0)]
        while stack:
            u, p, prev = stack.pop()
            base[u] = prev ^ mask(chars[u])
            for v in graph[u]:
                if v != p:
                    stack.append((v, u, base[u]))

        # Each node update affects its entire subtree's prefixes
        for u in range(n):
            range_xor(tin[u], tout[u], base[u])

        # Keep initial prefixes in a separate Fenwick structure
        # The difference structure above tracks changes only.
        bit = [0] * (n + 2)

        answer = []
        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                delta = mask(chars[u]) ^ mask(c)

                range_xor(tin[u], tout[u], delta)
                chars[u] = c

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                pu = base[u] ^ point_query(tin[u])
                pv = base[v] ^ point_query(tin[v])

                path_mask = pu ^ pv ^ mask(chars[w])

                # At most one odd-frequency character
                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer

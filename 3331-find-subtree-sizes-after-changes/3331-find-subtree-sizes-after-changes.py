class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        ans = [1] * n
        last = [-1] * 26
        prev = [-1] * n

        stack = [(0, False)]

        while stack:
            node, exiting = stack.pop()
            c = ord(s[node]) - ord('a')

            if not exiting:
                prev[node] = last[c]
                last[c] = node

                stack.append((node, True))

                for child in reversed(children[node]):
                    stack.append((child, False))

            else:
                last[c] = prev[node]

                new_parent = prev[node]
                if new_parent == -1:
                    new_parent = parent[node]

                if new_parent != -1:
                    ans[new_parent] += ans[node]

        return ans
class Solution:
    def maxDepth(self, s: str) -> int:
        ans,openbrackets=0,0
        for c in s:
            if c == '(':
                openbrackets+=1
            elif c == ")":
                openbrackets-=1
            ans=max(ans,openbrackets)
        return ans
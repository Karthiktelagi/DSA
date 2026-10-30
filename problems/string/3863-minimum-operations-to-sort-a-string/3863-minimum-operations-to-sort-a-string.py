
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Cannot sort the entire string in one operation
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Minimum is at the beginning or maximum at the end
        if s[0] == mn or s[-1] == mx:
            return 1

        # Minimum or maximum occurs in the middle
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2

        # Minimum is at the end and maximum is at the beginning
        return 3

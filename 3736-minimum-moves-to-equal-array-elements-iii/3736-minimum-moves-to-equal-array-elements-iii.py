class Solution:
    def minMoves(self, nums: List[int]) -> int:
        c = 0
        nums.sort()
        n = nums[-1]

        for i in nums:
            if i == n:
                continue
            else:
                c += n - i

        return c
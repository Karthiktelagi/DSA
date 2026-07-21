class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        max = sum
        for i in range(k, len(nums)):
            sum = sum + nums[i] - nums[i-k]
            if sum > max:
                max = sum
        return max / k
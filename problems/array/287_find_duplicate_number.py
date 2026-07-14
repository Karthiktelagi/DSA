"""
LeetCode 287. Find the Duplicate Number
Difficulty: Medium

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def findDuplicate(self, nums):
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
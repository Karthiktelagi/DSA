class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        # ans[x] will store the number of subarrays whose product % k == x
        ans = [0] * k 
        
        # dp[r] tracks the number of subarrays ending at the previous element with product % k == r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # Case 1: Start a new subarray with just the current number
            new_dp[num_mod] += 1
            
            # Case 2: Extend existing subarrays ending at the previous position
            for r in range(k):
                if dp[r] > 0:
                    new_mod = (r * num_mod) % k
                    new_dp[new_mod] += dp[r]
            
            # Accumulate the current counts into the total answer
            for r in range(k):
                ans[r] += new_dp[r]
                
            dp = new_dp
            
        return ans

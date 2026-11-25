class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        mod1, mod2 = 1_000_000_007, 1_000_000_009
        base = 911382323

        # Prefix hashes and powers
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i in range(n):
            h1[i + 1] = (h1[i] * base + nums[i]) % mod1
            h2[i + 1] = (h2[i] * base + nums[i]) % mod2
            p1[i + 1] = (p1[i] * base) % mod1
            p2[i + 1] = (p2[i] * base) % mod2

        # Check if a unique subarray of length L exists
        def check(L):
            count = {}

            for i in range(n - L + 1):
                j = i + L

                hash1 = (h1[j] - h1[i] * p1[L]) % mod1
                hash2 = (h2[j] - h2[i] * p2[L]) % mod2

                key = (hash1, hash2)
                count[key] = count.get(key, 0) + 1

            return any(v == 1 for v in count.values())

        # Binary search for the minimum valid length
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
# Notes

## Current Solution

- Uses an auxiliary list.
- Easy to understand.
- Accepted by LeetCode.

### Complexity

- Time: O(n²)
- Space: O(n)

Reason:

`num not in unique` performs a linear search every iteration.

---

## Optimal Solution

Use Two Pointers.

```python
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
```

### Complexity

- Time: O(n)
- Space: O(1)

This is the recommended interview solution.
# Notes

## Current Solution

- Uses two nested loops.
- Checks every pair.
- Easy to understand.
- Accepted by LeetCode.

### Complexity

- Time: **O(n²)**
- Space: **O(1)**

---

## Optimal Solution

Use a Hash Map (Dictionary).

```python
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[num] = i
```

### Complexity

- Time: **O(n)**
- Space: **O(n)**

---

## Interview Tip

Whenever you need to find two values that satisfy a condition (sum, difference, complement), think about using a **Hash Map** to reduce the time complexity from **O(n²)** to **O(n)**.
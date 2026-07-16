# Notes

## Current Solution

- Sort the array.
- Return the middle element.

Since the majority element appears more than half the time, it must occupy the middle position after sorting.

### Complexity

- Time: **O(n log n)**
- Space: **O(1)**

---

## Optimal Solution (Boyer-Moore Voting Algorithm)

```python
class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

---

## Why Boyer-Moore Works

The majority element appears more than half the time, so every occurrence of a different element can be paired with one occurrence of the majority element. After all pairings, the majority element remains as the final candidate.

---

## Interview Tip

Possible approaches:

1. Brute Force → O(n²)
2. Hash Map → O(n)
3. Sorting → O(n log n)
4. **Boyer-Moore Voting** → O(n), O(1) ✅ (Best)
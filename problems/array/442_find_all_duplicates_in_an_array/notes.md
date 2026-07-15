# Notes

## Current Solution

- Sort the array.
- Compare adjacent elements.
- Store duplicates in a list.

### Complexity

- Time: **O(n log n)**
- Space: **O(1)**

---

## Optimal Solution (Negative Marking)

```python
class Solution:
    def findDuplicates(self, nums):
        ans = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                ans.append(abs(num))
            else:
                nums[index] *= -1

        return ans
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

---

## Interview Tip

Whenever the problem states:

- Values are in the range **1 to n**
- Modify the array is allowed
- Constant extra space

Think about **Negative Marking** or **Cyclic Sort** techniques.
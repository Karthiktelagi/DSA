# Notes

## Current Solution

- Compare every element of `nums1` with every element of `nums2`.
- Mark matched elements as `None` to avoid duplicate matches.
- Simple and easy to understand.

### Complexity

- **Time:** O(n × m)
- **Space:** O(1)

---

## Optimal Solution (Hash Map)

```python
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        freq = Counter(nums1)
        ans = []

        for num in nums2:
            if freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

        return ans
```

### Complexity

- **Time:** O(n + m)
- **Space:** O(min(n, m))

---

## Follow-up

If both arrays are already sorted:

- Use the **Two Pointer** technique.

Complexity:

- **Time:** O(n + m)
- **Space:** O(1)

---

## Interview Tip

For intersection problems:

- **Unsorted arrays** → Hash Map
- **Sorted arrays** → Two Pointers
- **Brute force** → Nested loops (easy but slower)
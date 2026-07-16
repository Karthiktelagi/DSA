# Notes

## Current Solution

- Remove non-alphanumeric characters.
- Convert everything to lowercase.
- Compare the processed string with its reverse.

### Complexity

- Time: **O(n)**
- Space: **O(n)**

---

## Optimal Solution (Two Pointers)

```python
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

---

## Interview Tip

There are two common approaches:

1. Build a cleaned string and compare it with its reverse.
2. Use **Two Pointers** to compare characters in-place.

The two-pointer approach is preferred in interviews because it avoids extra space.
# Notes

## Current Solution

- Reverse every row.
- Invert each element.
- Modify the matrix in-place.

---

## Complexity

- **Time:** O(n²)
- **Space:** O(1)

---

## Alternative Approach

You can combine both operations into a single pass using two pointers.

Example:

```python
for row in image:
    left, right = 0, len(row) - 1

    while left <= right:
        if row[left] == row[right]:
            row[left] ^= 1
            row[right] ^= 1

        row[left], row[right] = row[right], row[left]
        left += 1
        right -= 1
```

This performs the horizontal flip and inversion together.

---

## Interview Tip

Remember the two operations:

1. Reverse the row.
2. Invert each bit.

A two-pointer solution can merge both steps into one traversal for a more optimized implementation.
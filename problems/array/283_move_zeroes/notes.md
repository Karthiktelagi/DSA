# Notes

## Idea

Keep all non-zero numbers at the beginning of the array while preserving their order.

### Steps

1. Initialize pointer `j = 0`.
2. Traverse the array.
3. If the current element is non-zero:
   - Swap `nums[i]` and `nums[j]`.
   - Increment `j`.

---

## Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## Why it works

- Every non-zero element is moved exactly once.
- Zeros naturally shift toward the end.
- The relative order of non-zero elements is preserved.

---

## Interview Tip

This is a classic **Two Pointer** problem.

Remember:

- `i` → scans the array.
- `j` → tracks where the next non-zero element should be placed.

This is the optimal solution expected in interviews.
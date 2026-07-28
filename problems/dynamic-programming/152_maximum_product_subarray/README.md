# 152. Maximum Product Subarray

- **Difficulty:** Medium
- **Topic:** Dynamic Programming, Array

---

## Problem

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

---

## Example 1

### Input

```text
nums = [2,3,-2,4]
```

### Output

```text
6
```

### Explanation

The subarray `[2,3]` has the largest product.

---

## Example 2

### Input

```text
nums = [-2,0,-1]
```

### Output

```text
0
```

---

## Approach

- Keep track of:
  - Maximum product ending at current index.
  - Minimum product ending at current index.
- A negative number swaps the maximum and minimum products.
- Update the answer after every iteration.

---

## Complexity

- **Time:** O(n)
- **Space:** O(1)
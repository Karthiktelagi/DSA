# 918. Maximum Sum Circular Subarray

- **Difficulty:** Medium
- **Topic:** Dynamic Programming, Array

---

## Problem

Given a circular integer array `nums`, return the maximum possible sum of a non-empty subarray.

A circular array means the end of the array connects to the beginning.

---

## Example 1

### Input

```text
nums = [1,-2,3,-2]
```

### Output

```text
3
```

### Explanation

The subarray `[3]` has the maximum sum.

---

## Example 2

### Input

```text
nums = [5,-3,5]
```

### Output

```text
10
```

### Explanation

The subarray `[5,5]` wraps around the array.

---

## Approach

- Use Kadane's Algorithm to find:
  - Maximum subarray sum.
  - Minimum subarray sum.
- Compute the total sum.
- The answer is:
  - `max_sum`
  - or `total_sum - min_sum` (wrap-around case).
- Handle the special case where all elements are negative.

---

## Complexity

- **Time:** O(n)
- **Space:** O(1)
# 560. Subarray Sum Equals K

- **Difficulty:** Medium
- **Topic:** Array, Prefix Sum, Hash Map

---

## Problem

Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

---

## Example 1

### Input

```text
nums = [1,1,1]
k = 2
```

### Output

```text
2
```

---

## Example 2

### Input

```text
nums = [1,2,3]
k = 3
```

### Output

```text
2
```

---

## Approach

- Maintain a running prefix sum.
- Store frequencies of prefix sums in a hash map.
- If `(current_prefix_sum - k)` exists in the map, then a valid subarray exists.
- Update the answer and continue.

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)
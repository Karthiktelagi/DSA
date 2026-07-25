# 88. Merge Sorted Array

- **Difficulty:** Easy
- **Topic:** Array, Two Pointers, Sorting

---

## Problem

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2`.

Merge `nums2` into `nums1` as one sorted array.

The final sorted array should not be returned. Instead, modify `nums1` in-place.

---

## Example

### Input

```text
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

### Output

```text
[1,2,2,3,5,6]
```

---

## Approach

1. Remove the extra zero placeholders.
2. Append all elements of `nums2`.
3. Sort the merged array.

---

## Complexity

- Time Complexity: **O((m+n) log(m+n))**
- Space Complexity: **O(1)** (modifies `nums1` in place)
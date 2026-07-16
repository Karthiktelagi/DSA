# 350. Intersection of Two Arrays II

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Array, Hash Table, Two Pointers, Sorting

---

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

Each element in the result must appear as many times as it appears in both arrays.

You may return the result in **any order**.

---

## Example 1

### Input

```text
nums1 = [1,2,2,1]
nums2 = [2,2]
```

### Output

```text
[2,2]
```

---

## Example 2

### Input

```text
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
```

### Output

```text
[4,9]
```

---

## Approach Used

1. Traverse every element of `nums1`.
2. Compare it with every element of `nums2`.
3. If a match is found:
   - Add it to the answer.
   - Mark the matched element in `nums2` as used (`None`).
   - Break to avoid counting it again.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n × m)** |
| Space | **O(1)** |

---

## Optimal Approach

Use a **Hash Map (Frequency Counter)**.

- Time: **O(n + m)**
- Space: **O(min(n,m))**

This is the preferred interview solution.
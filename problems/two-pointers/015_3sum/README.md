# 15. 3Sum

- **Difficulty:** Medium
- **Topic:** Array, Two Pointers, Sorting

## Problem

Given an integer array `nums`, return all the triplets
`[nums[i], nums[j], nums[k]]`
such that

- i != j
- i != k
- j != k

and

```
nums[i] + nums[j] + nums[k] == 0
```

The solution set must not contain duplicate triplets.

---

## Example

### Input

```text
nums = [-1,0,1,2,-1,-4]
```

### Output

```text
[[-1,-1,2],[-1,0,1]]
```

---

## Approach

1. Sort the array.
2. Fix one element.
3. Use two pointers (`left` and `right`) to search for the remaining two numbers.
4. Skip duplicate values to avoid duplicate triplets.

---

## Complexity

- Time: **O(n²)**
- Space: **O(1)** (excluding output)
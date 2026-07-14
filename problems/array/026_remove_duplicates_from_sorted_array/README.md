# 26. Remove Duplicates from Sorted Array

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Array, Two Pointers

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once.

Return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique elements in their original order.

---

## Example 1

### Input

```text
nums = [1,1,2]
```

### Output

```text
k = 2
nums = [1,2,_]
```

---

## Example 2

### Input

```text
nums = [0,0,1,1,1,2,2,3,3,4]
```

### Output

```text
k = 5
nums = [0,1,2,3,4,_,_,_,_,_]
```

---

## Approach Used

- Store unique elements in a temporary list.
- Copy the unique elements back into the original array.
- Return the number of unique elements.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | O(n²) |
| Space | O(n) |

> **Note:** This solution is accepted by LeetCode but is **not optimal** because checking `n not in list` is O(n).

---

## Optimal Approach

Use the **Two Pointer** technique.

- Time: **O(n)**
- Space: **O(1)**

This is the preferred interview solution.
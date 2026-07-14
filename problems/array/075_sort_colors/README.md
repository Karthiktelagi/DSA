# 75. Sort Colors

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Topic:** Array, Two Pointers, Sorting

## Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent.

Use the integers:

- `0` → Red
- `1` → White
- `2` → Blue

You must solve this problem **without using the library's sort function**.

---

## Example

### Input

```text
nums = [2,0,2,1,1,0]
```

### Output

```text
[0,0,1,1,2,2]
```

---

## Approach Used

Sort the array using Python's built-in `sort()`.

> **Note:** This approach passes on LeetCode but does **not** satisfy the follow-up requirement of avoiding the library sort.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | O(n log n) |
| Space | O(1) |

---

## Follow-up

Use the **Dutch National Flag Algorithm** for:

- Time: **O(n)**
- Space: **O(1)**
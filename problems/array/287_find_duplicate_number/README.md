# 287. Find the Duplicate Number

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Topic:** Array, Binary Search, Two Pointers, Floyd's Cycle Detection

## Problem

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`. Return this repeated number.

> Solve the problem without modifying the array and using only constant extra space.

---

## Example

### Input

```text
nums = [1,3,4,2,2]
```

### Output

```text
2
```

---

## Approach

1. Sort the array.
2. Compare adjacent elements.
3. Return the duplicate.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | O(n log n) |
| Space | O(1) |

---

## LeetCode

https://leetcode.com/problems/find-the-duplicate-number/
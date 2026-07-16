# 169. Majority Element

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Array, Hash Table, Divide and Conquer, Sorting, Boyer-Moore Voting Algorithm

---

## Problem Statement

Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than** `⌊n / 2⌋` times.

You may assume that the majority element always exists in the array.

---

## Example 1

### Input

```text
nums = [3,2,3]
```

### Output

```text
3
```

---

## Example 2

### Input

```text
nums = [2,2,1,1,1,2,2]
```

### Output

```text
2
```

---

## Approach Used

1. Sort the array.
2. The majority element always occupies the middle position after sorting.
3. Return the element at index `len(nums) // 2`.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n log n)** |
| Space | **O(1)** |

---

## Optimal Approach

Use the **Boyer-Moore Voting Algorithm**.

- Time: **O(n)**
- Space: **O(1)**

This is the optimal interview solution.
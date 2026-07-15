# 442. Find All Duplicates in an Array

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Topic:** Array, Hashing, Sorting

---

## Problem Statement

Given an integer array `nums` of length `n` where every integer is in the range `[1, n]` and each integer appears once or twice, return an array of all the integers that appear twice.

You must design an algorithm that runs in **O(n)** time and uses only **constant extra space** (excluding the output array).

---

## Example 1

### Input

```text
nums = [4,3,2,7,8,2,3,1]
```

### Output

```text
[2,3]
```

---

## Example 2

### Input

```text
nums = [1,1,2]
```

### Output

```text
[1]
```

---

## Example 3

### Input

```text
nums = [1]
```

### Output

```text
[]
```

---

## Approach Used

1. Sort the array.
2. Traverse the sorted array.
3. Compare adjacent elements.
4. If two adjacent elements are equal, add them to the answer.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n log n)** |
| Space | **O(1)** |

> **Note:** This solution is accepted but does **not** satisfy the follow-up requirement of **O(n)** time.

---

## Optimal Approach

Use the **Negative Marking** technique.

- Time: **O(n)**
- Space: **O(1)**

This is the expected interview solution.
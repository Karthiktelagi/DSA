# 1. Two Sum

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Array, Hash Table

---

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that:

- Exactly one solution exists.
- You may not use the same element twice.
- The answer can be returned in any order.

---

## Example 1

### Input

```text
nums = [2,7,11,15]
target = 9
```

### Output

```text
[0,1]
```

---

## Example 2

### Input

```text
nums = [3,2,4]
target = 6
```

### Output

```text
[1,2]
```

---

## Example 3

### Input

```text
nums = [3,3]
target = 6
```

### Output

```text
[0,1]
```

---

## Approach Used

Use two nested loops:

1. Select the first number.
2. Check every remaining number.
3. If their sum equals the target, return their indices.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n²)** |
| Space | **O(1)** |

---

## Optimal Approach

Use a **Hash Map (Dictionary)**.

- Time: **O(n)**
- Space: **O(n)**

This is the preferred interview solution.
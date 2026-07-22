# 53. Maximum Subarray

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Topic:** Dynamic Programming (Kadane's Algorithm)

---

## Problem Statement

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

---

## Example 1

### Input

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

### Output

```text
6
```

### Explanation

```text
[4,-1,2,1] = 6
```

---

## Example 2

### Input

```text
nums = [1]
```

### Output

```text
1
```

---

## Example 3

### Input

```text
nums = [5,4,-1,7,8]
```

### Output

```text
23
```

---

## Approach Used

Use Kadane's Algorithm.

- Keep a running sum.
- Reset the running sum when it becomes negative.
- Keep track of the maximum sum seen so far.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## Tags

- Array
- Dynamic Programming
- Kadane's Algorithm
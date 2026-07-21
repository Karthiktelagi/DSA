# 643. Maximum Average Subarray I

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Sliding Window

---

## Problem Statement

Given an integer array `nums` consisting of `n` elements and an integer `k`, find a contiguous subarray of length `k` that has the maximum average value and return this value.

---

## Example 1

### Input

```text
nums = [1,12,-5,-6,50,3], k = 4
```

### Output

```text
12.75
```

---

## Example 2

### Input

```text
nums = [5], k = 1
```

### Output

```text
5.0
```

---

## Approach Used

Use a Sliding Window.

- Compute the sum of the first `k` elements.
- Slide the window by:
  - Adding the new element.
  - Removing the leftmost element.
- Keep track of the maximum window sum.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## Tags

- Array
- Sliding Window
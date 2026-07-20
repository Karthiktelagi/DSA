# 338. Counting Bits

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Bit Manipulation, Dynamic Programming

---

## Problem Statement

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i (0 ≤ i ≤ n)`, `ans[i]` is the number of `1`s in the binary representation of `i`.

---

## Example 1

### Input

```text
n = 2
```

### Output

```text
[0,1,1]
```

### Explanation

```text
0 -> 0
1 -> 1
2 -> 10
```

---

## Example 2

### Input

```text
n = 5
```

### Output

```text
[0,1,1,2,1,2]
```

---

## Approach Used

Use Dynamic Programming.

For every number:

```text
bits(i) = bits(i >> 1) + (i & 1)
```

where

- `i >> 1` removes the last bit.
- `i & 1` checks whether the last bit is `1`.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## Tags

- Bit Manipulation
- Dynamic Programming
# 73. Set Matrix Zeroes

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Topic:** Matrix

---

## Problem Statement

Given an `m × n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`.

The operation must be performed **in-place**.

---

## Example 1

### Input

```text
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```

### Output

```text
[[1,0,1],
 [0,0,0],
 [1,0,1]]
```

---

## Example 2

### Input

```text
matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
```

### Output

```text
[[0,0,0,0],
 [0,4,5,0],
 [0,3,1,0]]
```

---

## Approach Used

- Traverse the matrix.
- Store all rows containing `0` in a set.
- Store all columns containing `0` in another set.
- Traverse again and set matrix cells to `0` if their row or column is marked.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(m × n)** |
| Space | **O(m + n)** |

---

## Tags

- Matrix
- Array
- Simulation
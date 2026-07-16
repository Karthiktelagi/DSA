# 832. Flipping an Image

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Array, Matrix, Simulation

---

## Problem Statement

Given an `n × n` binary matrix `image`, first flip the image horizontally, then invert it.

- Flip horizontally → Reverse each row.
- Invert → Replace every `0` with `1` and every `1` with `0`.

Return the resulting image.

---

## Example 1

### Input

```text
image = [[1,1,0],[1,0,1],[0,0,0]]
```

### Output

```text
[[1,0,0],[0,1,0],[1,1,1]]
```

---

## Example 2

### Input

```text
image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
```

### Output

```text
[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
```

---

## Approach

1. Traverse each row.
2. Reverse the row.
3. Invert every element:
   - `0 → 1`
   - `1 → 0`
4. Return the modified matrix.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n²)** |
| Space | **O(1)** |

---

## Tags

- Array
- Matrix
- Simulation
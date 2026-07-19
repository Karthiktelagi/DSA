# 191. Number of 1 Bits

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Bit Manipulation

---

## Problem Statement

Write a function that takes the binary representation of a positive integer and returns the number of set bits (`1`s) it has.

This is also known as the **Hamming Weight**.

---

## Example 1

### Input

```text
n = 11
```

### Binary

```text
1011
```

### Output

```text
3
```

---

## Example 2

### Input

```text
n = 128
```

### Binary

```text
10000000
```

### Output

```text
1
```

---

## Example 3

### Input

```text
n = 2147483645
```

### Output

```text
30
```

---

## Approach Used

Use **Brian Kernighan's Algorithm**.

Each operation

```text
n = n & (n - 1)
```

removes the **rightmost set bit**.

Count how many times this operation can be performed until `n` becomes `0`.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(k)** |
| Space | **O(1)** |

where `k` is the number of set bits.

---

## Tags

- Bit Manipulation
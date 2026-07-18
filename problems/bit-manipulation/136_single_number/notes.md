# Notes

## Current Solution

Use the XOR operator.

Rules:

```
a ^ a = 0
a ^ 0 = a
```

Duplicate numbers cancel each other.

Only the unique number remains.

---

## Example

Input

```text
[4,1,2,1,2]
```

Computation

```text
0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4
```

Answer

```text
4
```

---

## Why XOR Works

Suppose

```text
2 2 5 6 6
```

Then

```text
2 ^ 2 = 0
6 ^ 6 = 0
0 ^ 5 = 5
```

Duplicates disappear automatically.

---

## Complexity

- Time: **O(n)**
- Space: **O(1)**

---

## Interview Tip

Whenever a problem says:

- Every number appears twice
- Find the unique number
- O(n) time
- O(1) space

Think of **XOR** immediately.

Other common Bit Manipulation problems include:

- Single Number II
- Single Number III
- Number of 1 Bits
- Counting Bits
- Reverse Bits
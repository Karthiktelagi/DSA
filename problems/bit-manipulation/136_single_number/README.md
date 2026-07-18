# 136. Single Number

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Bit Manipulation, Array

---

## Problem Statement

Given a non-empty array of integers `nums`, every element appears twice except for one.

Find that single one.

You must implement a solution with:

- **Linear time complexity**
- **Constant extra space**

---

## Example 1

### Input

```text
nums = [2,2,1]
```

### Output

```text
1
```

---

## Example 2

### Input

```text
nums = [4,1,2,1,2]
```

### Output

```text
4
```

---

## Example 3

### Input

```text
nums = [1]
```

### Output

```text
1
```

---

## Approach Used

Use the XOR (`^`) operator.

Properties of XOR:

- `a ^ a = 0`
- `a ^ 0 = a`
- XOR is commutative and associative.

By XORing all elements together, duplicate numbers cancel each other out, leaving only the unique number.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## Tags

- Bit Manipulation
- Array
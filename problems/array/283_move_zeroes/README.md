# 283. Move Zeroes

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Array, Two Pointers

---

## Problem Statement

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements.

You must perform this operation **in-place** without making a copy of the array.

---

## Example 1

### Input

```text
nums = [0,1,0,3,12]
```

### Output

```text
[1,3,12,0,0]
```

---

## Example 2

### Input

```text
nums = [0]
```

### Output

```text
[0]
```

---

## Approach

Use the **Two Pointer** technique.

- Maintain a pointer `j` for the next position of a non-zero element.
- Traverse the array.
- Whenever a non-zero element is found, swap it with `nums[j]`.
- Increment `j`.

This keeps all non-zero elements in their relative order while moving zeros to the end.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## Tags

- Array
- Two Pointers
- In-place Algorithm
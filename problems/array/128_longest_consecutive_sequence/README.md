# 128. Longest Consecutive Sequence

- **Difficulty:** Medium
- **Topic:** Array, Sorting

---

## Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

---

## Example 1

### Input

```text
nums = [100,4,200,1,3,2]
```

### Output

```text
4
```

Explanation:

The longest consecutive sequence is `[1,2,3,4]`.

---

## Example 2

### Input

```text
nums = [0,3,7,2,5,8,4,6,0,1]
```

### Output

```text
9
```

---

## Approach

- Remove duplicates using `set()`.
- Sort the numbers.
- Traverse the sorted array.
- Count consecutive numbers.
- Keep track of the maximum length.

---

## Complexity

- **Time:** O(n log n)
- **Space:** O(n)
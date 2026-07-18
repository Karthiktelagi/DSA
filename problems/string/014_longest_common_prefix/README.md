# 14. Longest Common Prefix

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** String, Sorting

---

## Problem Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Example 1

### Input

```text
strs = ["flower","flow","flight"]
```

### Output

```text
"fl"
```

---

## Example 2

### Input

```text
strs = ["dog","racecar","car"]
```

### Output

```text
""
```

---

## Approach Used

1. Handle the empty array case.
2. Sort the array lexicographically.
3. Compare only the first and last strings.
4. Find the common prefix between them.
5. Return the matching prefix.

Since the array is sorted, the common prefix of the first and last strings is the common prefix of the entire array.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n log n + m)** |
| Space | **O(1)** |

where:

- `n` = number of strings
- `m` = length of the shortest string

---

## Tags

- String
- Sorting
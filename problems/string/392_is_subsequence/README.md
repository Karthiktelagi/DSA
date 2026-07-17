# 392. Is Subsequence

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** String, Two Pointers, Dynamic Programming

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence of a string is a new string generated from the original string by deleting some (or no) characters without changing the relative order of the remaining characters.

---

## Example 1

### Input

```text
s = "abc"
t = "ahbgdc"
```

### Output

```text
true
```

---

## Example 2

### Input

```text
s = "axc"
t = "ahbgdc"
```

### Output

```text
false
```

---

## Approach Used

1. Use two pointers:
   - `i` for string `s`
   - `j` for string `t`
2. Traverse `t`.
3. If characters match, move both pointers.
4. Otherwise, move only the pointer in `t`.
5. If all characters of `s` are matched, return `true`.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

where `n = len(t)`.

---

## Tags

- String
- Two Pointers
- Dynamic Programming
# 20. Valid Parentheses

- **Difficulty:** Easy
- **Topic:** Stack, String

---

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

A string is valid if:

1. Open brackets are closed by the same type.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

---

## Example 1

### Input

```text
s = "()"
```

### Output

```text
true
```

---

## Example 2

### Input

```text
s = "()[]{}"
```

### Output

```text
true
```

---

## Example 3

### Input

```text
s = "(]"
```

### Output

```text
false
```

---

## Approach

- Continuously remove valid pairs:
  - `()`
  - `[]`
  - `{}`
- Repeat until no more replacements are possible.
- If the string becomes empty, it is valid.

---

## Complexity

- Time: **O(n²)** (worst case due to repeated replacements)
- Space: **O(1)**
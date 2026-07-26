# 1047. Remove All Adjacent Duplicates In String

- **Difficulty:** Easy
- **Topic:** Stack, String

---

## Problem

You are given a string `s` consisting of lowercase English letters.

A duplicate removal consists of choosing two adjacent and equal letters and removing them.

Repeat this process until no adjacent duplicate characters remain.

Return the final string.

---

## Example 1

### Input

```text
s = "abbaca"
```

### Output

```text
"ca"
```

### Explanation

```
abbaca
→ aaca
→ ca
```

---

## Example 2

### Input

```text
s = "azxxzy"
```

### Output

```text
"ay"
```

---

## Approach

- Traverse the string.
- Maintain a stack.
- If the current character matches the top of the stack, remove the top.
- Otherwise, push the character.
- Join the stack to obtain the final string.

---

## Complexity

- Time: **O(n)**
- Space: **O(n)**
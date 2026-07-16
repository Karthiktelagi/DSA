# 125. Valid Palindrome

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** String, Two Pointers

---

## Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Example 1

### Input

```text
s = "A man, a plan, a canal: Panama"
```

### Output

```text
true
```

---

## Example 2

### Input

```text
s = "race a car"
```

### Output

```text
false
```

---

## Example 3

### Input

```text
s = " "
```

### Output

```text
true
```

---

## Approach Used

1. Create a new string.
2. Traverse every character.
3. Keep only alphanumeric characters.
4. Convert them to lowercase.
5. Compare the string with its reverse.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## Optimal Approach

Use the **Two Pointer** technique without creating a new string.

- Time: **O(n)**
- Space: **O(1)**
# 151. Reverse Words in a String

- **Platform:** LeetCode
- **Difficulty:** Medium
- **Topic:** String

---

## Problem Statement

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters.

The returned string should:

- Contain the words in reverse order.
- Have only one space between words.
- Have no leading or trailing spaces.

---

## Example 1

### Input

```text
s = "the sky is blue"
```

### Output

```text
"blue is sky the"
```

---

## Example 2

### Input

```text
s = "  hello world  "
```

### Output

```text
"world hello"
```

---

## Example 3

### Input

```text
s = "a good   example"
```

### Output

```text
"example good a"
```

---

## Approach Used

- Split the string into words.
- Reverse the list.
- Join using a single space.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## Tags

- String
- Two Pointers
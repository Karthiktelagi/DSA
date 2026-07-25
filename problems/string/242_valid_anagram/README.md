# 242. Valid Anagram

- **Difficulty:** Easy
- **Topic:** String, Hash Table

---

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word formed by rearranging the letters of another word using all the original letters exactly once.

---

## Example 1

### Input

```text
s = "anagram"
t = "nagaram"
```

### Output

```text
true
```

---

## Example 2

### Input

```text
s = "rat"
t = "car"
```

### Output

```text
false
```

---

## Approach

1. Count the frequency of every character in both strings.
2. Compare the two frequency maps.
3. If both maps are equal, the strings are anagrams.

---

## Complexity

- **Time:** O(n)
- **Space:** O(1) (fixed alphabet) / O(n) in the general case
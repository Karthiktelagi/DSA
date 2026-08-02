# 49. Group Anagrams

- **Difficulty:** Medium
- **Topic:** String, Hash Table

---

## Problem

Given an array of strings `strs`, group the anagrams together.

You can return the answer in any order.

---

## Example 1

### Input

```text
strs = ["eat","tea","tan","ate","nat","bat"]
```

### Output

```text
[["bat"],["nat","tan"],["ate","eat","tea"]]
```

---

## Example 2

### Input

```text
strs = [""]
```

### Output

```text
[[""]]
```

---

## Example 3

### Input

```text
strs = ["a"]
```

### Output

```text
[["a"]]
```

---

## Approach

- Create a hash map.
- For each string, count the frequency of each character.
- Convert the frequency array into a tuple.
- Use the tuple as the key.
- Store all strings with the same key together.

---

## Complexity

- **Time:** O(n × k)
- **Space:** O(n × k)

where:

- `n` = number of strings
- `k` = maximum string length
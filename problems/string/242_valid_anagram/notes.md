# Notes

## Algorithm

- Use Python's `Counter` from the `collections` module.
- `Counter` stores the frequency of each character.
- Compare the two counters directly.
- If they are equal, both strings contain the same characters with the same frequencies.

---

## Dry Run

Input

```text
s = "anagram"
t = "nagaram"
```

Counter(s)

```text
{'a':3,'n':1,'g':1,'r':1,'m':1}
```

Counter(t)

```text
{'a':3,'n':1,'g':1,'r':1,'m':1}
```

Comparison

```text
Equal → True
```

---

## Complexity

- Time: O(n)
- Space: O(1) (English lowercase letters)

---

## Pattern

- String
- Hash Table
- Frequency Counting

---

## Alternative Approaches

### 1. Sorting

```python
return sorted(s) == sorted(t)
```

Time: O(n log n)

Space: O(n)

### 2. Hash Table (Optimal)

Use `Counter` to compare character frequencies.

Time: O(n)

Space: O(1)
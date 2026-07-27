# Notes

## Algorithm

1. Store the previous version of the string.
2. Remove all occurrences of:
   - `()`
   - `[]`
   - `{}`
3. Repeat until no changes occur.
4. If the final string is empty, return `True`; otherwise return `False`.

---

## Dry Run

Input

```text
s = "({[]})"
```

Iteration 1

```text
({[]})
→ ({})
```

Iteration 2

```text
({})
→ ()
```

Iteration 3

```text
()
→ ""
```

Output

```text
True
```

---

## Complexity

- Time: O(n²)
- Space: O(1)

---

## Pattern

- Stack
- String Processing

---

## Better Approach

Use an actual stack and a hash map.

Time: **O(n)**

Space: **O(n)**

The stack approach is the standard interview solution.
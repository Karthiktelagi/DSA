# Notes

## Algorithm

1. Create an empty stack.
2. Traverse each character in the string.
3. If the stack is not empty and the current character equals the top of the stack:
   - Pop the top element.
4. Otherwise:
   - Push the current character.
5. Join the remaining characters in the stack.

---

## Dry Run

Input

```text
abbaca
```

Stack Operations

```text
a
ab
a
aa
(empty after removing aa)
c
ca
```

Output

```text
ca
```

---

## Complexity

- Time: O(n)
- Space: O(n)

---

## Pattern

- Stack
- String Processing
- Simulation

---

## Key Observation

The stack always contains the current valid string after removing all adjacent duplicates seen so far.
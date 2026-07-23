# Notes

## Idea

Python's `split()` automatically:

- Removes leading spaces.
- Removes trailing spaces.
- Converts multiple spaces into a single separator.

Then reverse the list of words and join them with one space.

---

## Dry Run

Input

```text
"  hello   world  "
```

After split

```text
["hello", "world"]
```

Reverse

```text
["world", "hello"]
```

Join

```text
"world hello"
```

---

## Complexity

- Time: **O(n)**
- Space: **O(n)**

---

## Pattern

- String
- Reverse Traversal
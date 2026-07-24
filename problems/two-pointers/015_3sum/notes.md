# Notes

## Algorithm

- Sort the array first.
- Iterate through each element.
- Use two pointers to find two numbers whose sum equals the negative of the current element.
- Skip duplicates for:
  - Current element
  - Left pointer
  - Right pointer

---

## Dry Run

Input

```text
[-1,0,1,2,-1,-4]
```

Sorted

```text
[-4,-1,-1,0,1,2]
```

Triplets found

```text
[-1,-1,2]
[-1,0,1]
```

---

## Complexity

- Time: O(n²)
- Space: O(1)

---

## Pattern

- Sorting
- Two Pointers
- Duplicate Handling
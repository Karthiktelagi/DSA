# Notes

## Algorithm

1. If the array is empty, return 0.
2. Remove duplicates using `set()`.
3. Sort the numbers.
4. Traverse the sorted array.
5. Count consecutive elements.
6. Update the maximum sequence length.

---

## Dry Run

Input

```text
[100,4,200,1,3,2]
```

After removing duplicates and sorting

```text
[1,2,3,4,100,200]
```

Traversal

```text
1 → 2 → 3 → 4
Length = 4

100
Length = 1

200
Length = 1
```

Answer

```text
4
```

---

## Complexity

- Time: O(n log n)
- Space: O(n)

---

## Pattern

- Array
- Sorting
- Consecutive Sequence

---

## Key Observation

Sorting places consecutive numbers together, making it easy to count the longest streak.

Although accepted, this approach is **O(n log n)** because of sorting.

The optimal solution uses a **Hash Set** to achieve **O(n)** time.
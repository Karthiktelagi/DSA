# Notes

## Algorithm

1. Initialize:
   - `max_prod`
   - `min_prod`
   - `answer`
2. Traverse the array.
3. If the current number is negative:
   - Swap `max_prod` and `min_prod`.
4. Update:
   - `max_prod`
   - `min_prod`
5. Update the overall maximum product.

---

## Dry Run

Input

```text
[2,3,-2,4]
```

| Current | Max Product | Min Product | Answer |
|---------:|------------:|------------:|-------:|
| 2 | 2 | 2 | 2 |
| 3 | 6 | 3 | 6 |
| -2 | -2 | -12 | 6 |
| 4 | 4 | -48 | 6 |

Output

```text
6
```

---

## Complexity

- Time: O(n)
- Space: O(1)

---

## Pattern

- Dynamic Programming
- Kadane's Algorithm Variant
- Running Maximum & Minimum

---

## Key Observation

A negative number can turn the smallest (most negative) product into the largest positive product, so both the maximum and minimum products must be tracked at each step.
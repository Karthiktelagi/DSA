# Notes

## Algorithm

1. Calculate the total sum of the array.
2. Use Kadane's Algorithm to find:
   - Maximum subarray sum.
   - Minimum subarray sum.
3. There are two possible answers:
   - Normal maximum subarray (`max_sum`)
   - Circular maximum (`total - min_sum`)
4. If all elements are negative, return `max_sum`.

---

## Dry Run

Input

```text
[5,-3,5]
```

Total

```text
7
```

Maximum Subarray

```text
7
```

Minimum Subarray

```text
-3
```

Circular Sum

```text
7 - (-3) = 10
```

Answer

```text
10
```

---

## Complexity

- Time: O(n)
- Space: O(1)

---

## Pattern

- Dynamic Programming
- Kadane's Algorithm
- Circular Array

---

## Key Observation

The maximum circular subarray equals:

```text
Total Sum - Minimum Subarray Sum
```

If every element is negative, `total - min_sum` becomes `0`, which is invalid. In that case, return `max_sum`.
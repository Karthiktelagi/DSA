# Notes

## Sliding Window

Instead of calculating every subarray sum from scratch:

```text
[1,12,-5,-6]
```

Slide the window one position:

```text
Remove 1
Add 50
```

New Sum

```text
new_sum = old_sum - nums[i-k] + nums[i]
```

This avoids recomputing the entire sum.

---

## Dry Run

nums = [1,12,-5,-6,50,3]

k = 4

Window 1

```text
1 + 12 - 5 - 6 = 2
```

Window 2

```text
2 - 1 + 50 = 51
```

Window 3

```text
51 - 12 + 3 = 42
```

Maximum Sum = 51

Average

```text
51 / 4 = 12.75
```

---

## Complexity

- Time: **O(n)**
- Space: **O(1)**

---

## Pattern

Sliding Window (Fixed Size)

Whenever the question asks for:

- Subarray of size K
- Maximum sum
- Minimum sum
- Average of K elements

Think of the **Sliding Window** technique.
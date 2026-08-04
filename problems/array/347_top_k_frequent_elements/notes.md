# Notes

## Algorithm

1. Count the frequency of every element.
2. Create frequency buckets.
3. Place each number into its corresponding bucket.
4. Traverse buckets from highest frequency.
5. Collect the first `k` frequent elements.

---

## Dry Run

Input

```text
nums = [1,1,1,2,2,3]
k = 2
```

Frequency Map

```text
1 → 3
2 → 2
3 → 1
```

Buckets

```text
1 : [3]
2 : [2]
3 : [1]
```

Traverse

```text
Frequency 3 → [1]
Frequency 2 → [2]
```

Answer

```text
[1,2]
```

---

## Complexity

- Time: O(n)
- Space: O(n)

---

## Pattern

- Hash Map
- Bucket Sort

---

## Key Observation

Instead of sorting frequencies (`O(n log n)`), bucket sort groups numbers by their frequency, allowing retrieval of the most frequent elements in linear time.
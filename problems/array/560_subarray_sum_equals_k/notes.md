# Notes

## Algorithm

1. Initialize a hashmap with `{0:1}`.
2. Traverse the array while maintaining the prefix sum.
3. Check if `(prefix_sum - k)` exists in the hashmap.
4. If yes, increase the answer by its frequency.
5. Store/update the current prefix sum frequency.

---

## Dry Run

Input

```text
nums = [1,1,1]
k = 2
```

Prefix Map

```text
{0:1}
```

Iteration

```text
sum=1 → store 1

sum=2
2-2=0 exists
count=1

sum=3
3-2=1 exists
count=2
```

Answer

```text
2
```

---

## Complexity

- Time: O(n)
- Space: O(n)

---

## Pattern

- Prefix Sum
- Hash Map
- Arrays

---

## Key Observation

If

```text
prefixSum(j) - prefixSum(i) = k
```

then

```text
prefixSum(i) = prefixSum(j) - k
```

A hashmap lets us find previous prefix sums in **O(1)** time.
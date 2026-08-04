# 347. Top K Frequent Elements

- **Difficulty:** Medium
- **Topic:** Array, Hash Map, Bucket Sort

---

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in any order.

---

## Example 1

### Input

```text
nums = [1,1,1,2,2,3]
k = 2
```

### Output

```text
[1,2]
```

---

## Example 2

### Input

```text
nums = [1]
k = 1
```

### Output

```text
[1]
```

---

## Approach

- Count the frequency of each element using a hash map.
- Create buckets where index = frequency.
- Store elements according to their frequency.
- Traverse buckets from highest frequency to lowest.
- Collect the first `k` elements.

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)
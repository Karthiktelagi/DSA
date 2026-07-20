# Notes

## Current Solution

Dynamic Programming.

Formula:

```text
ans[i] = ans[i >> 1] + (i & 1)
```

Explanation:

- `i >> 1` removes the last bit.
- `i & 1` returns:
  - 1 if last bit is set
  - 0 otherwise

---

## Example

For

```text
n = 5
```

| Number | Binary | Formula | Bits |
|--------:|:------:|:-------:|-----:|
|0|0|0|0|
|1|1|ans[0]+1|1|
|2|10|ans[1]+0|1|
|3|11|ans[1]+1|2|
|4|100|ans[2]+0|1|
|5|101|ans[2]+1|2|

Answer

```text
[0,1,1,2,1,2]
```

---

## Why It Works

Every number can be written as:

```text
i = (i >> 1) * 2 + last_bit
```

The bit count equals:

```text
bits(i >> 1) + last_bit
```

---

## Complexity

- Time: **O(n)**
- Space: **O(n)**

---

## Interview Tip

Useful bit operations:

```text
i >> 1   -> Divide by 2
i & 1    -> Check last bit
n & (n-1)-> Remove rightmost set bit
```

This DP relation is the expected interview solution because it computes all answers in linear time without recalculating bit counts.
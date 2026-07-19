# Notes

## Current Solution

Use **Brian Kernighan's Algorithm**.

The expression

```text
n & (n - 1)
```

removes the lowest (rightmost) set bit from the number.

Count how many times this operation is performed until `n` becomes zero.

---

## Example

Input

```text
11
```

Binary

```text
1011
```

Iteration 1

```text
1011
1010
----
1010
```

Iteration 2

```text
1010
1001
----
1000
```

Iteration 3

```text
1000
0111
----
0000
```

Total set bits

```text
3
```

---

## Why It Works

Every iteration removes exactly one set bit.

If there are `k` set bits, the loop runs exactly `k` times.

---

## Complexity

- Time: **O(k)**
- Space: **O(1)**

where `k` is the number of set bits.

---

## Alternative Solution

```python
class Solution:
    def hammingWeight(self, n):
        return bin(n).count("1")
```

Time: **O(32)**

Space: **O(1)**

---

## Interview Tip

Remember these common bit tricks:

```text
n & (n - 1)    -> Remove rightmost set bit
n & -n         -> Isolate rightmost set bit
n ^ n          -> 0
n ^ 0          -> n
```

Brian Kernighan's Algorithm is the preferred interview solution for counting set bits efficiently.
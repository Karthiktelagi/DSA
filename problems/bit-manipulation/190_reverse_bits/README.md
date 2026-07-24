# 190. Reverse Bits

**Difficulty:** Easy

## Problem
Reverse the bits of a given 32-bit unsigned integer.

### Example

**Input:**
```text
43261596
```

**Output:**
```text
964176192
```

## Approach
- Initialize `result = 0`.
- Iterate 32 times.
- Shift `result` left by 1 bit.
- Append the last bit of `n` using `(n & 1)`.
- Shift `n` right by 1 bit.
- Return `result`.

## Complexity

- **Time:** O(32) ≈ O(1)
- **Space:** O(1)
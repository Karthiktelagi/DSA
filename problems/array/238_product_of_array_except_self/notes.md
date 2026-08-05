# Notes

## Idea

Instead of using division:

- Store product of all elements to the left.
- Store product of all elements to the right.
- Multiply both products.

---

## Dry Run

nums = [1,2,3,4]

Prefix:

res = [1,1,2,6]

Postfix:

Final:

res = [24,12,8,6]

---

## Complexity

- Time: O(n)
- Space: O(1)

---

## Pattern

- Prefix Sum / Prefix Product
- Suffix Product
- Array

---

## Key Observation

The answer at each index equals:

Product of elements before it × Product of elements after it.

No division is required.

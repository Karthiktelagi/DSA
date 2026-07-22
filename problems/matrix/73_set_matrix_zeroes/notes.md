# Notes

## Idea

Use two sets:

- zero_rows
- zero_cols

First pass:

- Record every row and column that contains a zero.

Second pass:

- If a cell belongs to a recorded row or column, make it zero.

---

## Dry Run

Input

```text
1 1 1
1 0 1
1 1 1
```

After first traversal

```text
zero_rows = {1}
zero_cols = {1}
```

Second traversal

```text
1 0 1
0 0 0
1 0 1
```

---

## Complexity

- Time: **O(m × n)**
- Space: **O(m + n)**

---

## Better Solution

LeetCode also has an **O(1) space** solution using the first row and first column as markers.
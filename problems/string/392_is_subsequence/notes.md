# Notes

## Current Solution

Use two pointers.

- `i` points to string `s`
- `j` points to string `t`

Whenever characters match, move both pointers.

Otherwise, move only the pointer in `t`.

If `i` reaches the end of `s`, then `s` is a subsequence of `t`.

---

## Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## Dry Run

Input

```text
s = "abc"
t = "ahbgdc"
```

| i | j | s[i] | t[j] | Action |
|---|---|------|------|--------|
|0|0|a|a|Match → i++, j++|
|1|1|b|h|Move j|
|1|2|b|b|Match|
|2|3|c|g|Move j|
|2|4|c|d|Move j|
|2|5|c|c|Match|

`i == len(s)` → **True**

---

## Interview Tip

This is a classic **Two Pointer** problem.

If there are many queries with different `s` strings but the same `t`, preprocessing `t` can improve efficiency.
# Notes

## Algorithm

- Keep only the first `m` valid elements in `nums1`.
- Append every element from `nums2`.
- Sort the final array.

---

## Dry Run

Input

```text
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

After removing extra zeros

```text
[1,2,3]
```

After appending

```text
[1,2,3,2,5,6]
```

After sorting

```text
[1,2,2,3,5,6]
```

---

## Complexity

Time : O((m+n) log(m+n))

Space : O(1)

---

## Better Approach

Use the **Three Pointer** technique starting from the end of both arrays.

Time: **O(m+n)**

Space: **O(1)**
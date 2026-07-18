# Notes

## Current Solution

1. Sort the strings.
2. Compare only the first and last strings.
3. The common prefix between these two strings is the answer.

This works because sorting places the most different strings at the ends.

---

## Complexity

- **Time:** O(n log n + m)
- **Space:** O(1)

---

## Example

Input

```text
["flower","flow","flight"]
```

After Sorting

```text
["flight","flow","flower"]
```

Compare

```text
flight
flow
```

Matching characters

```text
f ✔
l ✔
i ✘ o
```

Answer

```text
fl
```

---

## Alternative Approach (Vertical Scanning)

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]
```

### Complexity

- Time: **O(n × m)**
- Space: **O(1)**

---

## Interview Tip

Common approaches:

1. Horizontal Scanning
2. Vertical Scanning ⭐
3. Sorting ⭐
4. Trie (advanced)

For interviews, **Vertical Scanning** is the most common solution, while the **Sorting** approach is concise and easy to implement.
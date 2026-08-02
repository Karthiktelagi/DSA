# Notes

## Algorithm

1. Create a dictionary.
2. For every string:
   - Count occurrences of each letter.
   - Convert the count array to a tuple.
   - Use the tuple as the key.
3. Append the string to the corresponding group.
4. Return all grouped values.

---

## Dry Run

Input

```text
["eat","tea","tan","ate","nat","bat"]
```

Keys

```text
eat → (1,0,0,...,1,...)

tea → same key

ate → same key

tan → different key

nat → same as tan

bat → different key
```

Output

```text
[
["eat","tea","ate"],
["tan","nat"],
["bat"]
]
```

---

## Complexity

- Time: O(n × k)
- Space: O(n × k)

---

## Pattern

- Hash Map
- String
- Character Frequency
- Grouping

---

## Key Observation

Two strings are anagrams if they have the same frequency of every character.

The frequency array uniquely identifies each anagram group.

Using a tuple allows it to be used as a dictionary key.
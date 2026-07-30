# Notes

## Algorithm

1. Create an empty list.
2. Traverse the linked list.
3. Store each node in the list.
4. Return the node at index `len(nodes) // 2`.

---

## Dry Run

Input

```text
1 → 2 → 3 → 4 → 5
```

Stored Nodes

```text
[1,2,3,4,5]
```

Middle Index

```text
5 // 2 = 2
```

Returned Node

```text
3 → 4 → 5
```

---

## Complexity

- Time: O(n)
- Space: O(n)

---

## Pattern

- Linked List
- Array Traversal

---

## Better Approach

Use two pointers:

- Slow moves one step.
- Fast moves two steps.

When `fast` reaches the end, `slow` points to the middle node.

Time: **O(n)**

Space: **O(1)**

This is the standard interview solution.
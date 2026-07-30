# 876. Middle of the Linked List

- **Difficulty:** Easy
- **Topic:** Linked List

---

## Problem

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

---

## Example 1

### Input

```text
head = [1,2,3,4,5]
```

### Output

```text
[3,4,5]
```

---

## Example 2

### Input

```text
head = [1,2,3,4,5,6]
```

### Output

```text
[4,5,6]
```

---

## Approach

1. Traverse the linked list.
2. Store every node in an array.
3. Return the node at index `len(nodes) // 2`.

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)
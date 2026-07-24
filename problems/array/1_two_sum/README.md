# 1. Two Sum

**Difficulty:** Easy

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

## Example

**Input**

```text
nums = [2,7,11,15]
target = 9
```

**Output**

```text
[0,1]
```

## Approach

- Use two nested loops.
- Check every pair of numbers.
- If their sum equals the target, return their indices.

## Complexity

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
# Notes

## Kadane's Algorithm

Maintain two values:

- current_sum
- max_sum

If current_sum becomes negative, reset it to 0 because a negative sum will only reduce the sum of future subarrays.

---

## Dry Run

nums = [-2,1,-3,4,-1,2,1,-5,4]

current_sum = 0

-2 → current = -2 → max = -2 → reset

1 → current = 1 → max = 1

-3 → current = -2 → reset

4 → current = 4 → max = 4

-1 → current = 3

2 → current = 5

1 → current = 6 → max = 6

-5 → current = 1

4 → current = 5

Answer = 6

---

## Why Not Sliding Window?

Sliding Window works when the window size is fixed or can be adjusted based on a condition.

Here, the optimal subarray can have **any length**, so Kadane's Algorithm is the optimal approach.

---

## Complexity

- Time: **O(n)**
- Space: **O(1)**

---

## Pattern

Dynamic Programming

Kadane's Algorithm
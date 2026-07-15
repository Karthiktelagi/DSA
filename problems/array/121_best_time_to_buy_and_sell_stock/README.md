# 121. Best Time to Buy and Sell Stock

- **Platform:** LeetCode
- **Difficulty:** Easy
- **Topic:** Array, Dynamic Programming

---

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a stock on the `i-th` day.

Choose a single day to buy one stock and choose a different future day to sell that stock.

Return the maximum profit you can achieve.

If no profit is possible, return `0`.

---

## Example 1

### Input

```text
prices = [7,1,5,3,6,4]
```

### Output

```text
5
```

Explanation:

- Buy on day 2 (price = 1)
- Sell on day 5 (price = 6)

Profit = 6 − 1 = 5

---

## Example 2

### Input

```text
prices = [7,6,4,3,1]
```

### Output

```text
0
```

No profitable transaction is possible.

---

## Approach

- Keep track of the minimum stock price seen so far.
- For each day:
  - Calculate the profit if sold today.
  - Update the maximum profit.
  - Update the minimum price if a lower price is found.

---

## Complexity

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## Tags

- Array
- Dynamic Programming
- Greedy
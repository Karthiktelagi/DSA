# Notes

## Key Idea

Track the lowest buying price seen so far while traversing the array once.

For every day's price:

- Compute the profit if sold today.
- Update the maximum profit.
- Update the minimum buying price if a lower price appears.

---

## Variables

- `min_price` → Lowest stock price encountered.
- `profit` → Profit if sold today.
- `max_profit` → Best profit seen so far.

---

## Complexity

- Time: **O(n)**
- Space: **O(1)**

---

## Why it works

The algorithm always considers buying before selling by maintaining the minimum price from previous days only.

---

## Interview Tip

This is a classic **Greedy** problem.

Remember:

- Keep the minimum buying price.
- Continuously calculate the current profit.
- Update the answer whenever a better profit is found.

This is the optimal interview solution.
# 238. Product of Array Except Self

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must solve it without using division and in O(n) time.

## Example

Input:
nums = [1,2,3,4]

Output:
[24,12,8,6]

## Approach

1. Create an answer array initialized with 1.
2. Traverse left to right while storing prefix products.
3. Traverse right to left while storing postfix products.
4. Multiply prefix and postfix products to get the final answer.

## Complexity

- Time: O(n)
- Space: O(1) (excluding output array)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []

        for num in arr:
            diff = abs(x - num)
            temp.append([num, diff])

        temp.sort(key=lambda x: (x[1], x[0]))

        ans = []

        for i in range(k):
            ans.append(temp[i][0])

        ans.sort()

        return ans
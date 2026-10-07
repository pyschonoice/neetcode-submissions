class Solution:
    def trap(self, num: List[int]) -> int:
        n = len(num)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = num[0]
        suffix[n-1] = num[n-1]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],num[i])
        #print(prefix)
        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1],num[i])

        #print(suffix)

        trapped_water = 0
        for i in range(n):
            trapped_water += min(prefix[i],suffix[i]) - num[i]
        return trapped_water
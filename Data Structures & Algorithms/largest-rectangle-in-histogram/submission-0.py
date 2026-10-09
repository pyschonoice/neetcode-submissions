class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        prev = [-1] * n
        for i in range(n):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                prev[i] = stk[-1]
            stk.append(i)

        nxt = [n] * n
        stk = []
        for i in range(n-1,-1,-1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk: nxt[i] = stk[-1]
            stk.append(i)

        max_area = 0
        for i in range(n):
            prev[i] +=  1
            nxt[i] -= 1
            max_area = max(max_area,heights[i]*(nxt[i]-prev[i]+1))
        
        return max_area

        

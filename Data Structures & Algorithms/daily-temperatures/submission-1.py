class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = []
        stk = []
        for i in range(len(temp)-1,-1,-1):
            while stk and temp[stk[-1]] <= temp[i]:
                stk.pop()
            if stk:
                result.append(stk[-1] - i)
            else: 
                result.append(0)
            stk.append(i)
            
        return result[::-1]
class Solution:
    def isValid(self, s: str) -> bool:
        mpp = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stk = []
        for ch in s:
            if ch in mpp.keys() and stk and mpp[ch] == stk[-1]:
                stk.pop()
                continue
            
            stk.append(ch)

        return True if len(stk) == 0 else False
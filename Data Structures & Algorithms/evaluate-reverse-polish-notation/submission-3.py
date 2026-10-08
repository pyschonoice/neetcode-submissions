class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = ("+","-","*","/")
        for ch in tokens:
            if ch in operators:
                second = int(stk.pop())
                first = int(stk.pop())
                if ch == "+":
                    new =  first + second
                if ch == "-":
                    new = first - second
                if ch == "*":
                    new = first * second
                if ch == "/":
                    new = int(first / second)
                stk.append(str(new))
                continue
            stk.append(ch)

        return int(stk[0])
class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
        self.min_element = float('inf')
    def push(self, val: int) -> None:

        self.min_element = min(self.min_element,val)
        self.min_stk.append(self.min_element)
        self.stk.append(val)
        


    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        if self.min_stk:
            self.min_element = self.min_stk[-1]
        else:
            self.min_element = float('inf')
            

        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
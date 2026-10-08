class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        car_arr = []
        for i in range(len(position)):
            car_arr.append((position[i],speed[i]))
        car_arr.sort(reverse=True)
        
        for pos,spe in car_arr:
            time_taken = (target - pos) / spe
            if stk and stk[-1] >= time_taken:
                continue
            stk.append(time_taken)

        return len(stk)
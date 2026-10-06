class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            comb = numbers[left] + numbers[right]
            if comb ==  target:
                return [left+1,right+1]
            if comb > target:
                right -= 1
            else:
                left += 1
            
        return [0,0]
            
            
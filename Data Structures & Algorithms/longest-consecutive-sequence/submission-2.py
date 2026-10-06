class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        lngest = set(nums)
        for num in lngest:
            if (num-1) not in lngest:
                length = 1
                while (num+length) in lngest:
                    length += 1
                result = max(length, result)
        return result

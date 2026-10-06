class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        lngest = set(nums)
        for i in range(len(nums)):
            num = nums[i]
            if num-1 not in lngest:
                cnt = 0
                while num in lngest:
                    cnt += 1
                    num += 1
                result = max(cnt,result)

        return result

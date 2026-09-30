class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mpp:
                return [mpp[complement],i]
            mpp[nums[i]] = i

        return [0,0]
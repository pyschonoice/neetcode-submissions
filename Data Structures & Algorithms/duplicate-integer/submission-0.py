class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp = {}
        for n in nums:
            if n in mpp:
                return True
            mpp[n] = 1

        return False
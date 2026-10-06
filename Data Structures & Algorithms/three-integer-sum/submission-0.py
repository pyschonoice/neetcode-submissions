class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        count = Counter(nums)
        for i in range(n):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                count[nums[j]] -= 1
                if j- 1 > i and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if count[target] > 0:
                    res.append([nums[i],nums[j],target])
            for j in range(i+1,n):
                count[nums[j]] += 1
        return res
            
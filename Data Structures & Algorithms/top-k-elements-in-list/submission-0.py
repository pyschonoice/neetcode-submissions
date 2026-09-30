class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stk = []
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1


        for num, count in freq.items():
            heapq.heappush(stk,(count,num))
            if len(stk) > k:
                heapq.heappop(stk)

        result = []
        for _ , n in stk:
            result.append(n)

        return result
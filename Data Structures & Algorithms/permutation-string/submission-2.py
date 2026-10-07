class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mpp = defaultdict(int)
        for i in range(len(s1)):
            mpp[s1[i]] += 1
        curr = defaultdict(int)
        if len(s1) > len(s2):
            return False
        window_size = len(s1)
        left = 0
        for right in range(len(s2)):
            curr[s2[right]] += 1
            if right-left+1 > window_size:
               curr[s2[left]] -= 1
               if curr[s2[left]] == 0:
                    del curr[s2[left]]
               left += 1
            if curr == mpp:
                return True

        return False
        

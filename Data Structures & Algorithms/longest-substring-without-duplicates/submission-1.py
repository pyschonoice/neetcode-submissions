class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = defaultdict(int)
        if len(s) == 0:
            return 0
        left = 0
        result = 0
        for i in range(len(s)):
            if s[i] in hashset:
                
                left = max(left,hashset[s[i]]+1)
            hashset[s[i]] = i
            result = max(result,i-left+1)

        return result
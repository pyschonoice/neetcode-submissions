class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mpp = defaultdict(int)
        max_freq = 0
        result = 0
        for i in range(len(s)):
            mpp[s[i]] += 1
            max_freq = max(max_freq, mpp[s[i]])
            replacement = (i - left + 1) - max_freq 
            if replacement > k:
                mpp[s[left]] -= 1
                left += 1
            result = max(result, i - left + 1)

        return result

            


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpp1 = {}
        mpp2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            mpp1[s[i]] = mpp1.get(s[i],0)+1
            mpp2[t[i]] = mpp2.get(t[i],0)+1

        return mpp1 == mpp2
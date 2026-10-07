class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freq = Counter(t)
        res = [-1,-1]
        resLen = float("inf")

        window = defaultdict(int)
        have, need = 0, len(freq)
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in freq and freq[s[right]] == window[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = (right - left + 1)
                    res = [left,right]
                window[s[left]] -= 1
                if s[left] in freq and freq[s[left]] > window[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left:right+1] if resLen != float("inf") else ""


                
            

            


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freq = Counter(t)
        window = defaultdict(int)

        res , resLen = [-1,-1], float("inf")
        left = 0
        have, need = 0, len(freq)

        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            if char in freq and window[char] == freq[char]:
                have += 1

            while have == need:
                if (right-left+1 )< resLen:
                    res = [ left, right]
                    resLen = right-left+1
                window[s[left]] -= 1
                if s[left] in freq and window[s[left]] < freq[s[left]]:
                    have -= 1
                left += 1

            
        left, right = res

        return s[left:right+1] if resLen != float("inf") else ""
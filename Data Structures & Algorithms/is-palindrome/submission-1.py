class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        
        print(new_str)
        size = len(new_str)
        i = 0
        while i < size//2:
            if new_str[i] != new_str[size-i-1]:
                return False

            i+= 1

        return True
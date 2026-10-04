class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + "#" + s)

        return "".join(encoded)
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != "#":
                j += 1

            # Get length
            size = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract string
            result.append(s[j:j + size])

            # Move to next encoded string
            i = j + size

        return result

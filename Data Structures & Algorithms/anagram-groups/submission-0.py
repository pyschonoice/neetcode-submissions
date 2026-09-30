class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mpp = {}
        for s in strs:
            ky = "".join(sorted(s))
            if ky in mpp:
                mpp[ky].append(s)
            else:
                mpp[ky] =[s]

        for x in mpp.values():
            result.append(x)

        return result

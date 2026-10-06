class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        left = 0
        right = n - 1
        while left < right:
            curr_area = min(heights[left], heights[right])*(right-left)
            area = max(curr_area,area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return area


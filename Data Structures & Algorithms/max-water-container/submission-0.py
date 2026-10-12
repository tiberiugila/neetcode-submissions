class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l, r = 0, len(heights) - 1
        while l < r:
            cont = (r-l) * min(heights[r],heights[l])
            best = max(best, cont)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return best
        
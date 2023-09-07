class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = res = 0
        r = len(height) - 1

        while l < r:
            h = min(height[l], height[r])
            area = h * (r - l)
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res
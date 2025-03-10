#Time Complexity : O(nlogn), where n is length of height
#Space Complexity : O(1), since it does not need extra space

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) -1
        
        area = 0 
        

        while start < end:
            width = end - start
            h = min(height[start], height[end])
            area = max(area, h* width)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1        

        return area
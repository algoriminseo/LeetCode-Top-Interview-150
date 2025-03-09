# I could not solve this by my own. I solved by watching videos ...
# Time Compelxity : O(n ^ 2), where n is length of the array. 
# Keep accessing items for i, left,and right pointers
# Space Compelxity : O(1) or O(n), depending on sorting method

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 <= nums.length <= 3000
        # -10^5 <= nums[i] <= 10^5 
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                total = num + nums[left] + nums[right]
                if total > 0:
                    right -= 1 
                elif total < 0:
                    left += 1
                else:  
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left -1] and left < right:
                        left += 1 

        return res
#Time Complexity : O(n), where n is length of array nums
#Space Complexity : O(n), where n is length of array nums. Have to allocate memory for the result array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        result = [1] * length


        left = 1
        for i in range(0, length):
            result[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
            


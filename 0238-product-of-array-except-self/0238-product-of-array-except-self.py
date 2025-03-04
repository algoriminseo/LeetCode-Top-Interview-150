#Time Complexity : O(n), where n is length of array nums
#Space Complexity : O(n), where n is length of array nums. Have to allocate memory for the result array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        total_prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_prod *= num
        for i in range(len(res)):
            if nums[i] == 0 and zero_count >= 2:
                res = [0] * len(nums)
                return res
            elif nums[i] == 0 and zero_count == 1:
                res = [0] * len(nums)
                res[i] = total_prod
                return res

            res[i] = total_prod // nums[i]
        return res


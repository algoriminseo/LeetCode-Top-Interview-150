#Time complexity : O(n), where n is length of nums
#Space complexity : O(1), since there is no need for extra spaces

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]

        return k + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time Complexity : O(n), where n is length of array
        # Space Complexity : O(1), since we do not need extra space
       
        k = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k 

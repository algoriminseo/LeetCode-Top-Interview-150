class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = list(set(nums))

        if len(nums) > len(nums2):
            return True
        return False
        


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i, num in enumerate(nums):
            other_val = target - nums[i]
            if other_val in hash_map:
                return [hash_map[other_val], i]
            hash_map[num] = i 

                
        return None

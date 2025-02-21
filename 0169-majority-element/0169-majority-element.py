class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        # times = len(nums) // 2
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        max_key = nums[0]
        max_val = freq[nums[0]]

        for x, y in freq.items():
            if max_val < y:
                max_val = y
                max_key = x
        
        return max_key
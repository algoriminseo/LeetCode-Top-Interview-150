class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Algorithm : referenced niits algorithm 
        #Time complexity : O(n), where n is length of nums
        #Space complexity : O(n), extra n spaces for rotated array
        
     
        n = len(nums)
        k = k % len(nums)
        rotated = [0] * n 

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        for k in range(n):
            nums[k] = rotated[k]

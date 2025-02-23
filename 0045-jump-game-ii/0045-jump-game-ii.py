# Referenced Other codes and tried by myself
# Algorithm : The main thing we need to know in this problem is that to get minimum jumps to nums[n-1],
# it is core approach to think of maximum distance to get through
# Time Complexity : O(n), where n is length of nums array
# Space Complexity : O(1), since the function states about the variables

class Solution:

    def jump(self, nums: List[int]) -> int:
        near = 0
        far = 0 
        jumps = 0   

        while far < len(nums) - 1 :
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])

            near = far + 1
            far = farthest
            jumps += 1

        return jumps 


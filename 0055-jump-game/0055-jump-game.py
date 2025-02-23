class Solution:
    #Time Compelxity : O(n) , where n is length of array
    #Space Compelxity : O(1), since it is just declaring variables
  
    def canJump(self, nums: List[int]) -> bool:


        goal = len(nums) -1  
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return goal == 0 
             
 



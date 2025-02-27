#Algorithm :
# 1. Applying first rule, initialize array values as 1
# 2. First track (left to right) Applying second rule, compare two values and the bigger one gets one candy
# 3. Second track (right to left) Apply second rule, but different. Getting candy for bigger value will violate second rule, so using max function will avoid this.
# 4. Sum up all values in candies
#Time Complexity : O(n), where n is length of ratings
#Space Complexity : O(n), where n is length of candies. Allocate extra space for new array


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i] , candies[i+1]+1)
        
        return sum(candies)






        


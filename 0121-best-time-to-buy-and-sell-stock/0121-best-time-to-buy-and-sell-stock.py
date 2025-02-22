#Time Complexity : O(n), where n is length of array Comparing with two pointers and worst case, it will access through all items in the array 
#Space Complexity : O(1), since it does not need extra space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0 

        for price in prices[1:]:
            if buy > price:
                buy = price
                
            max_profit = max(max_profit, price - buy )

        return max_profit
#Approach : Using two pointers starting from left to right and right to left
#TIme Complexity : O(n), where n is length of numbers
#Space Complexity : O(1), since it has constant space



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right: 
            total = numbers[left] + numbers[right]
            if target < total:
                right -= 1
            elif target > total:
                left += 1
            else:
                return [left +1, right + 1]
        
        return []
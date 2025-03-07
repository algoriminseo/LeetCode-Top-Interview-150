import re

#Time complexity : O(n) , where n is length of the array
#Space complexity : O(1), since we don't need extra space for comparing elements
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        
        start = 0
        end = len(strs)-1
        
        while start <= end:
            if strs[start] == strs[end]:
                start += 1
                end -= 1
            else:
                return False

        return True
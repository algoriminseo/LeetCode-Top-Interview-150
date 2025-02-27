#Time Compelxity : O(n), where n is length of nums
#Space Compelxity : O(n), where n is length of num2. In the worst case, if there is no duplicates, nums2 list will be created same as nums list.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in nums:
            if i in hash_table.keys():
                return True
            else :         
                hash_table[i] = i
        return False
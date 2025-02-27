#Time Compelxity : O(n), where n is length of nums
#Space Compelxity : O(n), where n is length of num2. In the worst case, if there is no duplicates, nums2 list will be created same as nums list.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)

        return False
    
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """



        #Time complexity : O(m + n) , where m, n is length of each list.
        #We need to compare each elements in the two arrays. 
        #Space complexity : O(1) It does not need extra space
        i = m - 1
        j = n - 1
        p = m + n -1
        while j >= 0 :
            if i>= 0 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        return nums1
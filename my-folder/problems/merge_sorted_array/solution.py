class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        nums1[m:m+n]=nums2[0:n]
        nums1.sort()
            
            
            
               
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
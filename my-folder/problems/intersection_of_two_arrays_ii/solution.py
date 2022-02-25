class Solution(object):
    def intersect(self, nums1, nums2):
        result=dict()
        for i in nums1:
            if i in result:
                result[i]+=1
            else:
                result[i]=1
        final=[]
        for i in nums2:
            if i in result and result[i]>0:
                final.append(i)
                result[i]-=1
        return final
                
        
        
        
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
class Solution(object):
    def validMountainArray(self, arr):
        
        #if len(arr)<3:return False
        #start=arr.index(max(arr))
        #if start==len(arr)-1:return False
        #if
        i=arr and arr.index(max(arr))
        return arr and 0<i<len(arr)-1 and all(a1<a2 for a1,a2 in zip(arr[:i],arr[1:i+1])) and all(a3>a4 for a3,a4 in zip(arr[i:],arr[i+1:])) or False
        """
        :type arr: List[int]
        :rtype: bool
        """
        
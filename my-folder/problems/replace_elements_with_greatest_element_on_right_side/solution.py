class Solution(object):
    def replaceElements(self, arr):
        n=len(arr)
        big=arr[n-1]
        arr[n-1]=-1
        for i in range(n-2,-1,-1):
            temp=arr[i]
            arr[i]=big
            if big<temp:big=temp
        return arr
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
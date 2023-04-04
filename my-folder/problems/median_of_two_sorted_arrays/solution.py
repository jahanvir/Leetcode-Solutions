class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        
        def merge(arr,l,m,r):
            n1=m-l+1
            n2=r-m

            L=arr[l:l+n1]
            R=arr[m+1:m+1+n2]

            i=0
            j=0
            k=l

            while i<n1 and j<n2:
                if L[i] <= R[j]:
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1

            while i<n1:
                arr[k] = L[i]
                i+=1
                k+=1
            
            while j<n2:
                arr[k] = R[j]
                j+=1
                k+=1

        def mergeSort(arr,l,r):
            if l<r:
                m=l+(r-l)//2

                mergeSort(arr,l,m)
                mergeSort(arr,m+1,r)
                merge(arr,l,m,r)

        arr=nums1+nums2
        n=len(arr)
        mergeSort(arr,0,len(arr)-1)
        
        if n%2==0:
            return (arr[n//2]+arr[(n//2)-1])/2
        else:
            return arr[n//2]


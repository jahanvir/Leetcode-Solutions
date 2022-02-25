class Solution(object):
    def findRestaurant(self, list1, list2):
        
        dic={}
        for item1 in list1:
            for item2 in list2:
                if item1==item2:
                    dic[item1]=list1.index(item1)+list2.index(item2)
        return [k for k in dic if dic[k]==min(dic.values())]
        
        
        
        
            
        
        
        
            
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
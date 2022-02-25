class MyHashSet(object):

    def __init__(self):
        self.hashset=[]
        

    def add(self, key):
        if self.contains(key)==False:
            self.hashset.append(key)
        """
        :type key: int
        :rtype: None
        """
        

    def remove(self, key):
        if self.contains(key):
            i=self.hashset.index(key)
            self.hashset.pop(i)
        """
        :type key: int
        :rtype: None
        """
        

    def contains(self, key):
        return key in self.hashset
        """
        :type key: int
        :rtype: bool
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
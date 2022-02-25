class MyHashMap(object):

    def __init__(self):
        self.hashmap=[-1]*1000001
        

    def put(self, key, value):
        self.hashmap[key]=value
        
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        

    def get(self, key):
        return self.hashmap[key]
        """
        :type key: int
        :rtype: int
        """
        

    def remove(self, key):
        self.put(key,-1)
        """
        :type key: int
        :rtype: None
        """
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
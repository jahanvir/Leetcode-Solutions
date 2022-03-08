class Solution(object):
    def isPalindrome(self, s):
        import string
        temp=[i.lower() for i in s if i in string.digits or i in string.ascii_letters]
        temp2=temp[::-1]
        return True if temp==temp2 else False
        

        """
        :type s: str
        :rtype: bool
        """
        
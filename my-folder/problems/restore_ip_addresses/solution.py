class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]

        def valid(start,path):
            if start==len(s) and len(path)==4:
                ans.append(path[0]+'.'+path[1]+'.'+path[2]+'.'+path[3])
                return
            
            if start == len(s) or len(path)==4:
                return

            for length in range(1,4):
                if start+length > len(s):
                    return
                
                if length >1 and s[start]== '0':
                    return

                num=s[start:start+length]

                if int(num) > 255:
                    return
                
                valid(start+length,path+[num])
                


        valid(0,[])
        return ans

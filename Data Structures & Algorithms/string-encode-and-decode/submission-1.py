class Solution:

    def encode(self, strs: List[str]) -> str:

        res=""
        for i in strs:
            res += str(len(i))+'#'+i
        return res

    def decode(self, s: str) -> List[str]:

        res=[]

        i=0
        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            length= int(s[i:j])
            i=1+j
            j=i+length
            res.append(s[i:j])
            i=j
        return res
        



    """
        4#neet4#code5#loves3#you
        i=0
        j=0

        j=1
        len=[0:1] excludes 1 = 4
        i=j+1 ==> i=2
        j=2+len ==> j=6

        res.append(s[i:j])

        i=j
        
    """






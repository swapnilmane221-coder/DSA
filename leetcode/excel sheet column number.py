class Solution(object):
    def titleToNumber(self, columnTitle):
        
        num=0
        for i in columnTitle:
            num=26*num+(ord(i)-ord("A")+1)
        return num

        

class Solution(object):
    def countTriples(self, n):
        count=0
        l=[i for i in range(1,n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j:
                    if (i**2+j**2)**0.5 in l:
                        count+=1
        return count
        
        
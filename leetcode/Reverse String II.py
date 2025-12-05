class Solution(object):
    def reverseStr(self, s, k):
        newl=[s[i:i+k] for i in range(0,len(s),k)]
        revl=""
        for i in range(len(newl)):
            if i%2==0:
                new=newl[i]
                revl+=new[::-1]
            else:
                revl+=newl[i]
        return revl
        
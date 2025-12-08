class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        revstr=[]
        for i in s:
            revstr.append(i[::-1])
        return " ".join(revstr)
        
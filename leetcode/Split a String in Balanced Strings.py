class Solution(object):
    def balancedStringSplit(self, s):
        split=0
        if len(s)<2:
            return 1

        r=0
        l=0
        for i in s:
            if i=="R":
                r+=1
            if i=="L":
                l+=1
            if r==l:
                split+=1
                r,l=0,0
        return split
        
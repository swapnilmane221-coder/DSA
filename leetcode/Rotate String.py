class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        if not s:
            return True
        s=s+s
        if goal in s:
            return True 
        return False
        
        
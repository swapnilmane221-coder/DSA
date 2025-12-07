class Solution(object):
    def firstUniqChar(self, s):
        hmap = {}
        for ch in s:
            hmap[ch] = hmap.get(ch,0) + 1
        for i, ch in enumerate(s):
            if hmap[ch] == 1:
                return i
        return -1
        
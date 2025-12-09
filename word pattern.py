class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        lst=s.split()
        dict={}
        if(len(lst)==len(pattern)):
            for i in range(len(lst)):
                if pattern[i] not in dict:
                    dict[pattern[i]]=lst[i]
                else:
                    if(dict[pattern[i]]!=lst[i]):
                        return False
        else:
            return False
        key=[i for i in dict.keys()]
        value=[i for i in dict.values()]
        print(key,value)
        print(dict)
        if(len(list(set(key)))==len(key) and len(list(set(value)))==len(key)):
            return True
        else:
            return False
        
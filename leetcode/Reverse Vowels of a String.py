class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ind=[]
        vowels=[]
        vowel="aeiouAEIOU"
        s=list(s)
        for i in range(len(s)):
            if s[i] in vowel:
                vowels.append(s[i])
                ind.append(i)
        j=len(vowels)-1
        for i in ind:
            s[i]=vowels[j]
            j-=1
        return "".join(s)
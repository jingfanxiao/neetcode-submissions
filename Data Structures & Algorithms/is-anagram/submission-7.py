class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        record=[0]*26
        for i in range (len(s)):
            record[ord(s[i])-ord('a')]+=1
            record[ord(t[i])-ord('a')]-=1
        for count in record:
            if count!=0:
                return False
        return True
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-97]+=1
            key = "".join(chr(i+97) * count[i] for i in range(26))

            if key not in groups:
                groups[key]=[s]
            else:
                groups[key].append(s)

        return list(groups.values())
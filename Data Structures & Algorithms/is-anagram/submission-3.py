class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS = {}
        mapT = {}

        for index, char in enumerate(s):
            charS = s[index]
            charT = t[index]
            mapS[charS] = mapS.get(charS, 0) + 1
            mapT[charT] = mapT.get(charT, 0) + 1

        return mapS == mapT
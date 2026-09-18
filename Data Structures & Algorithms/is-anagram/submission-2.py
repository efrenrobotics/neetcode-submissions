class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # conditions for being considered an anagram
        # string t is the same length as string s
        if len(s) != len(t):
            return False

        freqMap = {}
        num = 0

        for num in range(len(s)):
            freqMap[s[num]] = freqMap.get(s[num], 0) + 1
            freqMap[t[num]] = freqMap.get(t[num], 0) - 1

        for value in freqMap.values():
            if value != 0:
                return False
        return True
        
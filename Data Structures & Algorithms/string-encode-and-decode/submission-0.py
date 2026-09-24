class Solution:

    def encode(self, strs: List[str]) -> str:
        # the latin america encoder
        ans = ""
        for word in strs:
            ans += word + "ñ"
        return ans
        
    def decode(self, s: str) -> List[str]:
        idx = 0
        ans = []
        for index, letter in enumerate(s):
            if letter == "ñ":
                # create a string from idx to index
                word = s[idx:index]
                ans.append(word)
                idx = index + 1
                # add to ans list
        return ans
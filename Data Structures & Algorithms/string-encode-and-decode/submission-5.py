class Solution:

    def encode(self, strs: List[str]) -> str:
        # I want to come up with an encoding algorithm, where if I know the algorithm, I should
        # be able to decode our new word that we will be returning. 

        # My naive approach was to concatenate each word in the list, after we concatenate each 
        # word I would add a non-ascii character as a delimeter that the word 
        # I used the character 'ñ' as the delimeter for my latino algorithm

        # Now for encoding with a different algorithm, I want to add a '#' character followed by the length of the word so that we know where to take the substring from. 

        # ans, will be the string that we will be encoding and returning, concatinating words from the input list 
        ans = ""
        for word in strs:
            length = len(word)
            ans += str(length) + "#" + word
        return ans

    def decode(self, s: str) -> List[str]:
        # to decode our #number algorithm, we know that we need to return a list of words. 
        ans = []
        pos = 0
        while pos < len(s):
            delimeter_pos = pos
            while s[delimeter_pos] != '#':
                delimeter_pos += 1
            
            word_len = int(s[pos:delimeter_pos])

            word_start = delimeter_pos + 1
            word_end = word_start + word_len

            ans.append(s[word_start:word_end])

            pos = word_end
            
        return ans


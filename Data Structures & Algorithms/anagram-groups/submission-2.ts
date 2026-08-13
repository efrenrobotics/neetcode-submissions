class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        // map sorted word to an array of words
        // check if map contains current word sorted
        // map get array and add new word or default to empty array and add new word
        const map : Map<string, string[]> = new Map<string, string[]>();
        

        for(let i = 0; i < strs.length; i++) {
            const sortedWord : string  = strs[i].split('').sort().join('');
            let wordArray : string[] = map.get(sortedWord) ?? [];
            wordArray.push(strs[i])
            map.set(sortedWord, wordArray)
        }

        // iterate over keyset and build out ans
        let ans: string[][] = []
        for(const str of map.keys()) {
            ans.push(map.get(str))
        }
        return ans;
    }
}

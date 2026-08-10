class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if(s.length !== t.length) return false;

        let mapS : Map<string, number> = new Map<string, number>();
        let mapT : Map<string, number> = new Map<string, number>();
        
        for(let i = 0; i < s.length; i++) {
            mapS.set(s.charAt(i), (mapS.get(s.charAt(i)) ?? 0) + 1);
            mapT.set(t.charAt(i), (mapT.get(t.charAt(i)) ?? 0) + 1);
        }

        for(const [key, value] of mapS) {
            if(!mapT.has(key) || mapT.get(key) !== mapS.get(key)){
                return false;
            }
        }

        return true;
    }
}

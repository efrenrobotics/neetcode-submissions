class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // key = sorted word, value = list of anagrams
        HashMap<String, ArrayList<String>> map = new HashMap<>();

        for(String word : strs) {
            String sortedWord = sortString(word);
            if(!map.containsKey(sortedWord)) {
                map.put(sortedWord, new ArrayList<>());
            }
            map.get(sortedWord).add(word);
        }

        return new ArrayList<>(map.values());
    }

    private static String sortString(String str) {
        char[] charArr = str.toCharArray();
        Arrays.sort(charArr);
        return String.valueOf(charArr);
    }
}

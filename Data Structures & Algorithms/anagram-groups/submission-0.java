class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        ArrayList<List<String>> result = new ArrayList<>();
        // key = sorted word, value = list of anagrams
        HashMap<String, ArrayList<String>> map = new HashMap<>();

        for(String word : strs) {
            String sortedWord = sortString(word);
            if(map.containsKey(sortedWord)) {
                ArrayList<String> list = map.get(sortedWord);
                list.add(word);
                map.put(sortedWord, list);
            } else {
                ArrayList<String> list = new ArrayList<>();
                list.add(word);
                map.put(sortedWord, list);
            }
        }

        for(List<String> list : map.values()) {
            result.add(list);
        }

        return result;
    }

    private static String sortString(String str) {
        char[] charArr = str.toCharArray();
        Arrays.sort(charArr);
        return String.valueOf(charArr);
    }
}

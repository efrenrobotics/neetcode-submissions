class Solution {
    public int longestConsecutive(int[] nums) {
        // sort the array and find longest consecutive sequence. 
        // O(nlogn) time

        // [2, 20, 4, 10, 3, 4, 5]
        // add elements to a hash set 
        HashSet<Integer> set = new HashSet<>();
        for(int num : nums) {
            set.add(num);
        }
        // [2, 20, 4, 10, 3, 5]

        // Get the set, and see if the set contains cur + 1
        // I also have to worry about cur - 1 since you don't know which element
        // in list you got
        int consec = 0;

        for(int num : set) {
            if(!set.contains(num - 1)) {
                int curConsec = 1;
                while(set.contains(num + 1)) {
                    curConsec++;
                    num++;
                }
                consec = Math.max(consec, curConsec);
            }
        }
       
        return consec;
    }
}

class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Approach, go through each row, each col and each 3x3 box
        // each of the three cases maintain a map
        // map, cols : set<nums>
        // map, rows : set<nums>
        // map, boxes : set<nums>
        HashMap<Integer, Set<Integer>> rows = new HashMap<>();
        HashMap<Integer, Set<Integer>> cols = new HashMap<>();
        HashMap<Integer, Set<Integer>> squares = new HashMap<>();


        for(int r = 0; r < board.length; r++) {
            for(int c = 0; c < board[0].length; c++) {
                int curElement = board[r][c];
                if(curElement == '.') continue;

                // Rows
                if(!rows.containsKey(r)) {
                    HashSet<Integer> set = new HashSet<>();
                    set.add(curElement);
                    rows.put(r, set);
                } else {
                    if(rows.get(r).contains(curElement)) return false;
                    rows.get(r).add(curElement);
                }

                // Cols
                if(!cols.containsKey(c)) {
                    HashSet<Integer> set = new HashSet<>();
                    set.add(curElement);
                    cols.put(c, set);
                } else {
                    if(cols.get(c).contains(curElement)) return false;
                    cols.get(c).add(curElement);
                }

                // Squares
                if(!squares.containsKey((r/3) * 3 + c/3)) {
                    HashSet<Integer> set = new HashSet<>();
                    set.add(curElement);
                    squares.put((r/3) * 3 + c/3, set);
                } else {
                    if(squares.get((r/3) * 3 + c/3).contains(curElement)) return false;
                    squares.get((r/3) * 3 + c/3).add(curElement);
                }
            }
        }
        return true;
    }
}

class Solution {
    int[][] directions = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int numIslands(char[][] grid) {
        boolean[][] seen = new boolean[grid.length][grid[0].length];
        Queue<int[]> q = new LinkedList<>();
        int islands = 0;

        for(int r = 0; r < grid.length; r++) {
            for(int c = 0; c < grid[0].length; c++) {
                if(grid[r][c] == '1' && !seen[r][c]) {
                    // BFS find all neighbors of this islands
                    islands++;
                    q.add(new int[]{r,c});
                    while(!q.isEmpty()) {
                        int[] coordinate = q.remove();
                        int row = coordinate[0];
                        int col = coordinate[1];
                        for(int[] direction : directions) {
                            int nextRow = row + direction[0];
                            int nextCol = col + direction[1];
                            if(isValid(nextRow, nextCol, grid) && grid[nextRow][nextCol] == '1' && !seen[nextRow][nextCol]) {
                                q.add(new int[]{nextRow,nextCol});
                                seen[nextRow][nextCol] = true;
                            }
                        }
                    }
                }
            }
        }

        return islands;

    }

    public boolean isValid(int row, int col, char[][] grid) {
        return row < grid.length && row >= 0 && col >= 0 && col < grid[0].length;
    }
}

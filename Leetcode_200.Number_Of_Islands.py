class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid) == 0:
            return 0
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    mark_island(grid, i, j, len(grid), len(grid[0]))
                    count += 1
                    
        return count
    
def mark_island(grid, i, j, m, n):
    
    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
        return
    
    grid[i][j] = '2'
    
    mark_island(grid, i, j + 1, m, n)
    mark_island(grid, i, j - 1, m, n) 
    mark_island(grid, i+1, j, m, n)
    mark_island(grid, i-1, j, m, n)
    

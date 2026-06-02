#CS350HW7
#Nikki Rudnick, 5/28/2026
#PSU CS350 
#Homework #7

import copy # Imported to handle in-place grid modifications safely

'''
Constraints:

    n == grid[i].length, n represents the height of a column
    m == grid.length, m represents the length of a row
    1 <= n, m <= 300
    any element in the grid at grid[i][j] is either a '0' or a '1'
'''

'''GOAL: You are given an m x n matrix representing a grid map of land and water. 
The land is represented by any element in the grid with a value of '1', and the 
water is represented by any element in the grid with a value of '0'. Every element 
in the array must be populated with either a '1' or a '0', making this a binary grid.

An island is surrounded by water and formed by connecting adjacent land elements horizontally or vertically. 
You can assume that all four edges of the grid are all surrounded by water.
Develop a function that takes in an m x n matrix (the grid) as an argument, and returns the total number of islands 
found in that matrix.  We don't need to know what elements make up the islands, just how many islands exist. 
You may solve this problem using any algorithmic approach that you want, in any time complexity that you want. '''

def main(): 
    # ---------------------------------------------------------
    # TEST CASE 1
    # ---------------------------------------------------------
    m1 = 4
    n1 = 4
    ans1 = 2
    grid1 = [
      ["1","1","0","1"],
      ["1","1","0","1"],
      ["1","1","0","0"],
      ["0","0","0","0"]
    ]

    # ---------------------------------------------------------
    # TEST CASE 2
    # ---------------------------------------------------------
    m2 = 7
    n2 = 5
    ans2 = 4
    grid2 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["0","0","0","0","0"],
      ["0","0","0","0","0"],
      ["1","0","1","1","1"],
      ["0","0","0","0","1"],
      ["1","0","0","0","1"],
    ]

    # ---------------------------------------------------------
    # TEST CASE 3
    # ---------------------------------------------------------
    m3 = 4
    n3 = 2
    ans3 = 1
    grid3 = [
      ["0","0"],
      ["0","0"],
      ["1","1"],
      ["0","0"]
    ]

    # ---------------------------------------------------------
    # TEST CASE 4
    # ---------------------------------------------------------
    m4 = 7
    n4 = 6
    ans4 = 6
    grid4 = [
      ["1","0","0","1","0","0"],
      ["1","0","0","1","0","1"],
      ["1","0","0","0","0","0"],
      ["0","0","0","0","0","0"],
      ["0","0","1","0","0","0"], 
      ["1","0","0","0","0","1"],
      ["1","1","0","0","0","1"],
    ]

    # ---------------------------------------------------------
    # TEST CASE 5
    # ---------------------------------------------------------
    m5 = 4
    n5 = 5
    ans5 = 1
    grid5 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]

    # ---------------------------------------------------------
    # TEST CASE 6
    # ---------------------------------------------------------
    m6 = 4
    n6 = 5
    ans6 = 3
    grid6 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]

    # Combine into iterable lists
    test_m = [m1, m2, m3, m4, m5, m6]
    test_n = [n1, n2, n3, n4, n5, n6]
    test_ans = [ans1, ans2, ans3, ans4, ans5, ans6]
    test_grid = [grid1, grid2, grid3, grid4, grid5, grid6]

    # Testing Loop

    for i in range(len(test_grid)):
        print(f"--- Test {i + 1} ---")
        
        # Deepcopy ensures the original test grid isn't destroyed by graph traversal
        grid_copy = copy.deepcopy(test_grid[i])
        
        ans = numIslands(grid_copy)
        
        if ans == test_ans[i]:
            print(f"Output: {ans}")
            print("GOOD\n")
        else:
            print(f"Output:   {ans}")
            print(f"Expected: {test_ans[i]}")
            print("BAD\n")

def recursive_search(grid, r, c, rows, cols):
    #if we are out of bounds return
    if r >= rows or c >= cols:
        return 
    if r < 0 or c < 0:
        return 
    if grid[r][c] == "1":
        grid[r][c] = "0"  # Mark as visited by "sinking" it to water
        #check all 4 conected directions for land (recursivley)
        recursive_search(grid, r, c+1, rows, cols)
        recursive_search(grid, r, c-1, rows, cols)
        recursive_search(grid, r+1, c, rows, cols)
        recursive_search(grid, r-1, c, rows, cols)
    return

def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    # Loop through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find unvisited land, we found a new island!
            if grid[r][c] == "1":
                islands += 1
                recursive_search(grid, r, c, rows, cols)#mark all connected "1"s to "0"s

    return islands
'''
def recursive_search(grid, r, c, r_max, c_max, rows, cols):
    #if we are out of bounds return
    if r >= rows or c >= cols:
        return 
    if r < 0 or c < 0:
        return 
    if grid[r][c] == "0": #if weve reached the edge of the island
        if r_max < r:
            r_max = r # record max r reached to avoid re-checking
        if c_max < c:
            c_max = c # record max c reached to avoid re-checking
    if grid[r][c] == "1":
        grid[r][c] = "0"  # Mark as visited by "sinking" it to water
        #check all 4 conected directions for land (recursivley)
        recursive_search(grid, r, c+1, r_max, c_max, rows, cols)
        recursive_search(grid, r, c-1, r_max, c_max, rows, cols)
        recursive_search(grid, r+1, c, r_max, c_max, rows, cols)
        recursive_search(grid, r-1, c, r_max, c_max, rows, cols)
    return

def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    # Loop through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find unvisited land, we found a new island!
            if grid[r][c] == "1":
                islands += 1
                r_max = 0
                c_max = 0
                recursive_search(grid, r, c, r_max, c_max, rows, cols)#mark all connected "1"s to "0"s
                if r_max != 0:#increment r based on max value reached in recursion
                    r = r_max
                if c_max != 0:#increment c based on max value reached in recursion
                    c = c_max

    return islands'''
if __name__ == "__main__":

    main()
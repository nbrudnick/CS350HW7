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

def recursive_search(grid, r, c, r_max, c_max):
    #if we are out of bounds return
    if r >= len(grid) or c >= len(grid[0]):
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
        #check all 4 conected directions for land (recusrivly)
        recursive_search(grid, r, c+1, r_max, c_max)
        recursive_search(grid, r, c-1, r_max, c_max)
        recursive_search(grid, r+1, c, r_max, c_max)
        recursive_search(grid, r-1, c, r_max, c_max)
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
                recursive_search(grid, r, c, r_max, c_max)#mark all connected "1"s to "0"s
                if r_max != 0:#increment r based on max value reached in recursion
                    r = r_max
                if c_max != 0:#increment c based on max value reached in recursion
                    c = c_max

    return islands
'''
def mat_BFS(adj_mat, n, m):
    component_sizes = []

    # Loop through every single node in the graph
    for h in range(n):
        # If it's unvisited, we've possibly found a brand new connected component
        if adj_max[h] == False:
            #check the col for at least one '1' value,
            for k in range(m):
                if adj_mat[h][k] != 0:
                    component = bfs(adj_mat, total_nodes, h, visited)
                    component_sizes.append(len(component))
                    break
    return component_sizes


def bfs(adj_matrix, total_nodes, start_node, visited):
    #---NEW!----make an empty order array---#
    order = []
    #make my empty queue
    queue = []
    #push start node to the queue
    queue.append(start_node)
    #VISIT IT! We visit as we add!
    visited[start_node] =True
    order.append(start_node)

    while queue:
        current_node = queue.pop() #grabs from the end
        if visited[current_node] == False:
            #this current_node has not yet been visited
            #visit the node
            visited[current_node] = True
            order.append(current_node)

            #loop over the neighbors and push all unvisited to the stack
            #----THIS IS THE SECTION DIFFERENT FROM AN ADJACENCY LIST----#
            #row we want to iterate is the adjacency matrix at current node
            neighbor = 0 #each column is a potential neighbor node
            while neighbor < total_nodes: #row and column length will always be total_nodes
                if visited[neighbor] == False and adj_matrix[current_node][neighbor] == "1":
                    #if this element is a 1, it is a neighbor or current
                    #append it if it is unvisited
                    queue.append(neighbor)
                neighbor += 1

    return order
 '''
'''#Start the BFS loop
    while queue:
        current_node = queue.pop(0) #grabs from the front of the queue
        #loop over the neighbors and push all unvisited to the stack
        neighbor_list = adj_list[current_node]
        length_neighbor_list = len(neighbor_list)
        index = 0
        while index < length_neighbor_list:
            neighbor = neighbor_list[index]
            if visited[neighbor] == False:
                #VISIT as we add to the queue
                queue.append(neighbor)
                visited[neighbor] = True
                order.append(neighbor)
            index += 1

    print(f"The visited array shows we have seen each node: {visited}")
    print(f"The order we visited the nodes: {order}")'''

'''
def dfs_mat(adj_matrix, total_nodes, start_node, visited):

    order = []
    #make my empty stack
    stack = []
    #push start node to the stack
    stack.append(start_node)

    #Start the DFS loop
    while stack:
        current_node = stack.pop() #grabs from the end
        if visited[current_node] == False:
            #this current_node has not yet been visited
            #visit the node
            visited[current_node] = True
            order.append(current_node)

            #loop over the neighbors and push all unvisited to the stack
            #----THIS IS THE SECTION DIFFERENT FROM AN ADJACENCY LIST----#
            #row we want to iterate is the adjacency matrix at current node
            neighbor = 0 #each column is a potential neighbor node
            while neighbor < total_nodes: #row and column length will always be total_nodes
                if visited[neighbor] == False and adj_matrix[current_node][neighbor] == 1:
                    #if this element is a 1, it is a neighbor or current
                    #append it if it is unvisited
                    stack.append(neighbor)
                neighbor += 1

    return order

def adj_DPF(adj_list, total_nodes):
    visited = [False] * total_nodes
    component_sizes = []

    # Loop through every single node in the graph
    for start_node in range(total_nodes):
        # If it's unvisited, we've found a brand new connected component
        if visited[start_node] == False:
            component = dfs_adj(adj_list, start_node, visited)
            component_sizes.append(len(component))
    
    return component_sizes

def dfs_adj(adj_list, start_node, visited):

    order = []
    #make my empty stack
    stack = []
    #push start node to the stack
    stack.append(start_node)

    #Start the DFS loop
    while stack:
        current_node = stack.pop() #grabs from the end
        if visited[current_node] == False:
            #this current_node has not yet been visited
            #visit the node
            visited[current_node] = True
            order.append(current_node)

            #loop over the neighbors and push all unvisited to the stack
            neighbor_list = adj_list[current_node]
            length_neighbor_list = len(neighbor_list)
            index = 0
            while index < length_neighbor_list:
                neighbor = neighbor_list[index]
                if visited[neighbor] == False:
                    stack.append(neighbor)
                index += 1

    return order
'''
if __name__ == "__main__":

    main()
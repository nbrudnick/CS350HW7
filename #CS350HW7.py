#CS350HW7
#Nikki Rudnick, 5/28/2026
#PSU CS350 
#Homework #7

'''
Constraints:

The test graphs are be represented as an adjacency matrix and as an adjacency list
The test graphs are simple graphs (no self edges or multiple edges between nodes)
The test graphs are unweighted graphs (no weight values assigned to any of the edges)
The test graphs are not directional (there are no directions assigned to any of the edges)
The test graphs may either be fully connected (a path exists from any node, to any other node) or disconnected. 
Solution using the adjacency matrix must run in no worse than O(V2), where V is the cardinality (number) of Verticies in the graph and E is the cardinality (number) of Edges in the graph.
Solution using the adjacency list must run in no worse than O(V + E) time, where V is the cardinality (number) of Verticies in the graph and E is the cardinality (number) of Edges in the graph.

Each solution must run in no worse than O(V2) or O(V + E) time, where 
V is the cardinality (number) of Vertices (nodes) in the graph and 
E is the cardinality (number) of Edges in the graph.
For this homework a main calling routine that tests your function on at least one example graph is required.
'''

'''GOAL: return an array (or Python List) storing the sizes (number of nodes) of each component found, 
in the order in which they were found. The size of this array (or Python List) tells you how many 
connected components exist, and the values stored in the array tell you how many nodes are in each.'''
def main(): 
    # ---------------------------------------------------------
    # TEST CASE 1
    # ---------------------------------------------------------
    n1 = 11
    ans1 = [11]
    adj1 = [
        [9],                # Node 0
        [2, 5, 7],          # Node 1
        [1, 3, 5, 6, 8],    # Node 2
        [2, 6],             # Node 3
        [5, 8, 9],          # Node 4
        [1, 2, 4],          # Node 5
        [2, 3],             # Node 6
        [1],                # Node 7
        [2, 4],             # Node 8
        [4, 10],            # Node 9
        [9, 0]              # Node 10
    ]
    mat1 = [ 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0], 
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0], 
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] 
    ]

    # ---------------------------------------------------------
    # TEST CASE 2
    # ---------------------------------------------------------
    n2 = 6
    ans2 = [3, 3]
    adj2 = [
        [5],       # Node 0
        [5],       # Node 1
        [3, 4],    # Node 2
        [2, 4],    # Node 3
        [2, 3],    # Node 4
        [0, 1]     # Node 5
    ]
    mat2 = [ 
        [0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 1, 1, 0], 
        [0, 0, 1, 0, 1, 0], 
        [0, 0, 1, 1, 0, 0], 
        [1, 1, 0, 0, 0, 0] 
    ]

    # ---------------------------------------------------------
    # TEST CASE 3
    # ---------------------------------------------------------
    n3 = 10
    ans3 = [6, 4]
    adj3 = [
        [7],             # Node 0
        [3, 5],          # Node 1
        [4],             # Node 2
        [1, 5],          # Node 3
        [2, 7],          # Node 4
        [1, 3, 6],       # Node 5
        [5],             # Node 6
        [0, 4, 8, 9],    # Node 7
        [7],             # Node 8
        [7]              # Node 9
    ]
    mat3 = [ 
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    ]

    # ---------------------------------------------------------
    # TEST CASE 4
    # ---------------------------------------------------------
    n4 = 11
    ans4 = [11]
    adj4 = [
        [1],                               # Node 0
        [0, 2, 3, 4, 5, 6, 7, 8, 9, 10],   # Node 1
        [1],                               # Node 2
        [1],                               # Node 3
        [1],                               # Node 4
        [1],                               # Node 5
        [1],                               # Node 6
        [1],                               # Node 7
        [1],                               # Node 8
        [1],                               # Node 9
        [1]                                # Node 10
    ]
    mat4 = [ 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    ]

    # ---------------------------------------------------------
    # TEST CASE 5
    # ---------------------------------------------------------
    n5 = 9
    ans5 = [3, 4, 2]
    adj5 = [
        [1],          # Node 0
        [0, 2],       # Node 1
        [1],          # Node 2
        [4, 5, 6],    # Node 3
        [3],          # Node 4
        [3],          # Node 5
        [3],          # Node 6
        [8],          # Node 7
        [7]           # Node 8
    ]
    mat5 = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 1, 0] 
    ]

    # ---------------------------------------------------------
    # TEST CASE 6
    # ---------------------------------------------------------
    n6 = 13
    ans6 = [4, 2, 3, 1, 3]
    adj6 = [
        [1, 3],      # Node 0
        [0, 2],      # Node 1
        [1, 3],      # Node 2
        [0, 2],      # Node 3
        [5],         # Node 4
        [4],         # Node 5
        [7, 8],      # Node 6
        [6, 8],      # Node 7
        [6, 7],      # Node 8
        [],          # Node 9
        [11],        # Node 10
        [10, 12],    # Node 11
        [11]         # Node 12
    ]
    mat6 = [ 
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] 
    ]

    # Combine into iterable lists
    test_n = [n1, n2, n3, n4, n5, n6]
    test_adj = [adj1, adj2, adj3, adj4, adj5, adj6]
    test_mat = [mat1, mat2, mat3, mat4, mat5, mat6]
    test_ans = [ans1, ans2, ans3, ans4, ans5, ans6]

    # Testing Loop
    for i in range(len(test_n)):
        print(f"--- Test {i + 1} ---")
        
        ans1 = mat_DPF(test_mat[i], len(test_mat[i][0]))
        ans2 = adj_DPF(test_adj[i], len(test_adj[i]))
        
        # Comparing sorted arrays just in case your graph traversal 
        # finds connected components in a different order
        if sorted(ans1) == sorted(ans2) == sorted(test_ans[i]):
            print(f"Output1: {ans1}")
            print(f"Output2: {ans2}")
            print("GOOD\n")
        else:
            print(f"Output1:   {ans1}")
            print(f"Output2:   {ans2}")
            print(f"Expected: {test_ans[i]}")
            print("BAD\n")

def mat_DPF(adj_mat, total_nodes):
    visited = [False] * total_nodes
    component_sizes = []

    # Loop through every single node in the graph
    for start_node in range(total_nodes):
        # If it's unvisited, we've found a brand new connected component
        if visited[start_node] == False:
            component = dfs_mat(adj_mat, total_nodes, start_node, visited)
            component_sizes.append(len(component))

    return component_sizes

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

if __name__ == "__main__":

    main()
This code implements a clustering algorithm (Kruskal's algorithm) for computing a max-spacing k-clustering. The input file should describe a distance function (equivalently, a complete graph with edge costs) and have the following format: 

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j) for each choice of 1≤i<j≤n, where n is the number of nodes. For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. 
The script outputs the maximum spacing of a k-clustering as well as shows the clusters themselves. 


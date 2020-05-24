In the worst case, we would look at all of the edges in the direction of the goal vertex until we reach the goal vertex. We would look at b edges for every vertex in our search for close to d iterations. Thus, the runtime is O(bd).


A* ALGORITHM: CONCEPTUAL
Review of A*

The A* algorithm is a greedy graph search algorithm that optimizes looking for a target vertex.
A* is a modification of Dijkstra’s done by adding the estimated distance of each vertex to the goal vertex when searching.

We can modify Dijkstra’s and turn it into A* by changing the following:

Adding a target for the search.

Gathering possible optimal paths and identify a single shortest path.

Implementing a heuristic that determines the likely distance remaining.

The runtime of A* is O(bd) where b is the branching factor of the graph and d is the depth of the goal vertex from the start vertex.

A* is an introductory glimpse into artificial intelligence.
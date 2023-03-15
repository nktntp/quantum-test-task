# Problem statement
Calculate the number of islands in a matrix $M\times N$ that represents a map. There are 2 possible states on the map:
- 1 - Island 
- 0 - Ocean

If the cells of type "Island" are adjacent then they belong to the same island.

# Solution
This problem was solved using DFS algorithm. We iterate over matrix applying a sequence of actions:

1. If cell is not "visited". 
   1. If cell is of type "Island". Call `dfs` to mark all cells from this island as "visited". Increment number of islands.
   2. If cell is of type "Ocean". Mark cell as "visited".
   
The time complexity of the solution is $O(M*N)$ 






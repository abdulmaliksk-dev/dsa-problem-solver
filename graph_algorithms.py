"""
Graph Algorithms Implementation
Author: Abdul Malik Sk
"""

from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """Add an edge to the graph"""
        self.graph[u].append(v)
    
    def bfs(self, start):
        """
        Breadth-First Search
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """
        Depth-First Search
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        result = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result

# Test the algorithms
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("BFS starting from vertex 2:", g.bfs(2))
    print("DFS starting from vertex 2:", g.dfs(2))
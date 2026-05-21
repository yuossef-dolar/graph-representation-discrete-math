# """
# Graph Theory Project - MATH113/MATH211
# Tanfiz BFS, DFS, w Graph Visualization
# Mabny 3ala Rosen's Discrete Mathematics, Chapter 10
# Team: [yuossef hany fathy - 241002308 ,zyead mohamed - 241001031 , karem mohamed - 241000977,kareem sameh -231001126,amr saiad -241002638]
# """

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    """Class 3ashan yemathal graph best3'dam adjacency list"""
    
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        """Add vertex lel graph"""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, v1, v2):
        """Add undirected edge ben v1 w v2"""
        self.add_vertex(v1)
        self.add_vertex(v2)
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
        if v1 not in self.adj_list[v2]:
            self.adj_list[v2].append(v1)
    
    def bfs(self, start):
        """
        Tanfiz Breadth-First Search
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        if start not in self.adj_list:
            return []
        
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in sorted(self.adj_list[vertex]):  # sorted 3ashan el output yeb2a ثابت
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start, visited=None, result=None):
        """
        Tanfiz Depth-First Search (recursive)
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        if visited is None:
            visited = set()
        if result is None:
            result = []
        
        if start not in self.adj_list:
            return result
        
        visited.add(start)
        result.append(start)
        
        for neighbor in sorted(self.adj_list[start]):
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)
        
        return result
    
    def visualize(self, title="Graph Visualization", highlight_path=None):
        """
        Rasem el graph best3'dam matplotlib w networkx
        Momken kaman te3mel highlight le path mo3ayan (zay natig BFS)
        """
        G = nx.Graph()
         
        # Add kol el edges
        for vertex, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                G.add_edge(vertex, neighbor)
        
        # Layout algorithm 3ashan el positioning yeb2a sabett
        pos = nx.spring_layout(G, seed=42, k=0.5)
        
        # Rasem el nodes w edges
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
        nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        
        # Highlight lel path law mawgood
        if highlight_path and len(highlight_path) > 1:
            path_edges = list(zip(highlight_path, highlight_path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, 
                                   edge_color='red', width=3, style='dashed')
            nx.draw_networkx_nodes(G, pos, nodelist=highlight_path, 
                                   node_color='orange', node_size=900)
        
        plt.title(title, fontsize=14, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def __str__(self):
        """String representation lel adjacency list"""
        result = "Adjacency List:\n"
        for vertex in sorted(self.adj_list.keys()):
            result += f"  {vertex}: {sorted(self.adj_list[vertex])}\n"
        return result


# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    # Create graph zay el example: A→B→C→F→G
    g = Graph()
    
    # Add edges (undirected graph)
    edges = [
        ('A', 'B'), ('A', 'D'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'E'),
        ('E', 'F'),
        ('F', 'G')
    ]
    
    for v1, v2 in edges:
        g.add_edge(v1, v2)
    
    # E3rad el adjacency list
    print(g)
    
    # Tashgheel BFS men vertex 'A'
    bfs_result = g.bfs('A')
    print(f"BFS Traversal (starting from A): {' -> '.join(bfs_result)}")
    
    # Tashgheel DFS men vertex 'A'
    dfs_result = g.dfs('A')
    print(f"DFS Traversal (starting from A): {' -> '.join(dfs_result)}")
    
    # Visualize lel graph
    g.visualize(title="Graph Theory Project - Full Graph")
    
    # Visualize ma3 highlight lel BFS path
    g.visualize(title="BFS Path Highlighted (A → ... → G)", highlight_path=bfs_result)
    
    # Optional: Eظهار Handshaking Theorem verification
    total_degree = sum(len(neighbors) for neighbors in g.adj_list.values())
    num_edges = len(edges)
    print(f"\n🔍 Handshaking Theorem Verification:")
    print(f"   Sum of degrees = {total_degree}")
    print(f"   2 × |E| = 2 × {num_edges} = {2 * num_edges}")
    print(f"   ✓ Theorem holds: {total_degree == 2 * num_edges}")
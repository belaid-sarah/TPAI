import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from geopy.distance import geodesic

def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph.neighbors(node):
                stack.append((neighbor, path + [neighbor]))
    
    return None

# Fetch graph data for a region (e.g., a city or area in Algeria) from OpenStreetMap
def fetch_graph(place_name):
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph

# Get the node nearest to the specified location
def get_nearest_node(graph, location):
    point = ox.geocode(location)
    nearest_node = ox.distance.nearest_nodes(graph, point[1], point[0])
    return nearest_node

# Example usage
def main():
    # Define the locations (cities) between which you want to find the shortest path
    location1 = "Béjaïa, Algeria"
    location2 = "Bouira, Algeria"
    
    # Fetch the graph data for the specified regions (cities)
    graph = fetch_graph(location1)
    
    # Get the nodes nearest to the specified locations
    node1 = get_nearest_node(graph, location1)
    node2 = get_nearest_node(graph, location2)
    
    # Find the shortest path using DFS
    shortest_path = dfs(graph, node1, node2)
    
    # Print the shortest path
    if shortest_path:
        print("Shortest path from", location1, "to", location2, ":", shortest_path)
    else:
        print("No path found between", location1, "and", location2)
    
    # Visualize the graph with the shortest path highlighted
    ox.plot_graph_route(graph, shortest_path, route_color='red', route_linewidth=2, node_size=0)
    plt.show()

if __name__ == "__main__":
    main()

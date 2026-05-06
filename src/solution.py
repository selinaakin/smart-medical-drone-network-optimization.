import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("data/network_data.csv")

# Create graph
G = nx.Graph()

# Add edges
for index, row in data.iterrows():
    G.add_edge(
        row['source'],
        row['target'],
        weight=row['travel_time']
    )

# Define source and destination
source_node = "Main Medical Distribution Center"
destination_node = "Hospital D - Fatih"

# Calculate shortest path
shortest_path = nx.shortest_path(
    G,
    source=source_node,
    target=destination_node,
    weight='weight'
)

# Calculate shortest distance
shortest_distance = nx.shortest_path_length(
    G,
    source=source_node,
    target=destination_node,
    weight='weight'
)

# Print results
print("Shortest Path:", shortest_path)
print("Minimum Travel Time:", shortest_distance)

# Visualization
plt.figure(figsize=(14, 8))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightblue',
    node_size=3000,
    font_size=8,
    font_weight='bold'
)

# Edge labels
labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels
)

# Highlight shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=path_edges,
    edge_color='red',
    width=4
)

plt.title("Emergency Medical Drone Network Optimization")

plt.show()

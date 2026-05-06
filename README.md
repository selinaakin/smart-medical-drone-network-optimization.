# Smart Emergency Medical Drone Network Optimization for Istanbul

## 1. Real-World Problem Context

Large metropolitan cities such as Istanbul experience serious traffic congestion and operational delays in emergency healthcare logistics. Hospitals and healthcare organizations require fast transportation systems for blood packs, vaccines, emergency medication, organs, and laboratory samples.

This project focuses on a smart emergency medical drone delivery network that connects hospitals, laboratories, emergency coordination centers, and drone charging stations.

The project demonstrates how Management Information Systems (MIS) and network optimization models can improve healthcare operations and emergency response efficiency.

---

## 2. Problem Definition

The healthcare organization aims to optimize emergency medical deliveries between healthcare facilities using drones.

The primary objective is to:

- Minimize delivery time
- Improve operational efficiency
- Optimize healthcare logistics
- Support emergency decision-making

The project models the healthcare infrastructure as a weighted network structure.

---

## 3. Network Model

The project uses a weighted network model.

- Nodes represent healthcare locations
- Edges represent drone transportation routes
- Edge weights represent travel time in minutes

The network contains:

- 8 nodes
- 12 weighted edges

The project is based on the Shortest Path Optimization Model.

---

## 4. Nodes and Edges

## Nodes

| Node ID | Description |
|---|---|
| 1 | Main Medical Distribution Center |
| 2 | Drone Charging Station - Besiktas |
| 3 | Emergency Laboratory - Sisli |
| 4 | Hospital A - Kadikoy |
| 5 | Hospital B - Uskudar |
| 6 | Hospital C - Bakirkoy |
| 7 | Emergency Coordination Center |
| 8 | Hospital D - Fatih |

---

## Edges

| Source | Target | Travel Time |
|---|---|---|
| 1 | 2 | 6 |
| 1 | 3 | 8 |
| 2 | 4 | 7 |
| 2 | 5 | 5 |
| 3 | 5 | 4 |
| 3 | 6 | 9 |
| 4 | 7 | 6 |
| 5 | 7 | 3 |
| 5 | 8 | 7 |
| 6 | 8 | 5 |
| 7 | 8 | 4 |
| 4 | 5 | 2 |

---

## 5. Selected Algorithm

The selected optimization model is:

# Shortest Path Algorithm

The algorithm determines the minimum travel-time route between the source node and destination node.

The project uses weighted edge values to calculate the shortest cumulative route.

The selected source node is:

- Main Medical Distribution Center (Node 1)

The selected destination node is:

- Hospital D - Fatih (Node 8)

---

## 6. Python Implementation

The project was implemented using Python.

The following libraries were used:

```python
pandas
networkx
matplotlib

Main implementation steps:

Read CSV dataset
Create weighted graph
Add nodes and edges
Apply shortest path algorithm
Calculate total travel time
Visualize optimized route

## 7. Results

The shortest route calculated by the algorithm is:

Shortest Path: [1, 2, 5, 7, 8]
Minimum Travel Time: 18

This means the fastest emergency drone route is:

Main Medical Distribution Center → Besiktas Charging Station → Hospital B → Emergency Coordination Center → Hospital D

The optimized route minimizes emergency delivery time.

## 8. Managerial Interpretation

The project demonstrates how network optimization models can support healthcare management decisions.

The system may help managers:

Improve emergency response time
Reduce operational delays
Improve healthcare logistics efficiency
Support real-time routing decisions
Optimize resource utilization

This project also demonstrates the importance of MIS-supported operational analytics in smart healthcare systems.

## 9. How to Run the Code
Step 1

Install required libraries:

pip install -r requirements.txt
Step 2

Run the Python file:

python solution.py

## 10. References
Taylor, B. W. Introduction to Management Science
NetworkX Official Documentation
Healthcare Logistics Optimization Studies
Smart City Transportation Research

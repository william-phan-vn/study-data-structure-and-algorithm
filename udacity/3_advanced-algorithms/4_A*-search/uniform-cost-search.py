''' Uniform Cost Search - Cheapest First Search
Pick the path with the lowest total cost'''

import math
from typing import List, Dict


class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []
        self.is_frontier = False
        self.explored = False

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_road(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)

    # def remove_edge(self, node1, node2):
    #     if node1 in self.nodes and node2 in self.nodes:
    #         node1.remove_child(node2)
    #         node2.remove_child(node1)


class TrackingRoutes(object):
    def __init__(self, start: int):
        self.routes_dict: Dict[int: List[int]] = {start: [start]}

    def add_next_paths(self, last_node, next_nodes: List):
        temp_route = self.routes_dict[last_node]
        self.routes_dict.pop(last_node)
        for node in next_nodes:
            self.routes_dict[node] = temp_route + [node]

    def remove_route_by_last_node(self, last_node):
        self.routes_dict.pop(last_node)


class Map:
    def __init__(self, intersections, roads):
        self.intersections = intersections
        self.roads = roads


# def uniform_cost_search(graph: Graph, start_node, end_node, distance_dict={}, shortest_distance=0, shortest_path={}):
def uniform_cost_search(graph: Graph, start_node, end_node, tracking_route: TrackingRoutes, fontier_nodes_dict={}, lowest_total_cost=0):
    '''

    Args:
        graph:
        start_node:
        end_node:
        distance_dict: a dictionary that stores the distance to edge nodes wrt the start_node in the form of node:distance as key:value
        shortest_distance: the shortest distance road between start_node and end_node
        tracking_paths: the shortest path from start node to end node

    Returns:
        shortest_distance, shortest_path
    '''

    '''Starting exploring the space'''

    # Set the start_node in the graph as explored
    graph.nodes[start_node.value].is_frontier = True

    # Go through the Frontier path and Define the path_cost_list
    next_node_values = []
    for edge in start_node.edges:
        node_value = edge.node.value

        if not graph.nodes[node_value].is_frontier and not graph.nodes[node_value].explored:
            total_distance = edge.distance + lowest_total_cost
            fontier_nodes_dict[edge.node] = total_distance
            graph.nodes[node_value].is_frontier = True

            # Update the storing of current paths
            next_node_values.append(node_value)

    # If there is no edge added --> remove from the current path
    if len(next_node_values) > 0:
        tracking_route.add_next_paths(start_node.value, next_node_values)
    else:
        tracking_route.remove_route_by_last_node(start_node.value)


    # If the path_cost_dict is empty: There's no road between 2 city
    if len(fontier_nodes_dict) == 0:
        return None

    # Short the path cost to find the min cost
    current_node, node_distance = sorted(fontier_nodes_dict.items(), key=lambda x: x[1])[0]

    # Check if the current_node is the end_node
    if current_node.value == end_node.value:
        return tracking_route.routes_dict[current_node.value]

    # Update the frontier and the explored node
    graph.nodes[current_node.value].explored = True
    fontier_nodes_dict.pop(current_node)

    # Go through the cheapest cost path, repeat the uniform cost search
    return uniform_cost_search(graph, current_node, end_node, tracking_route, fontier_nodes_dict, node_distance)


def dijkstra(graph, start_node, end_node):
    # Create a dictionary that stores the distance to all nodes in the form of node:distance as key:value
    # Assume the initial distance to all nodes is infinity.
    # Use math.inf as a predefined constant equal to positive infinity
    distance_dict = {node: math.inf for node in graph.nodes}

    shortest_distance = {}

    distance_dict[start_node] = 0

    # 5. Create a `path` dictionary that keeps track of the previous node (value) that can lead to the current node (key).
    path = []

    while distance_dict:

        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        print(current_node.value, node_distance)

        path.append(current_node.value)
        shortest_distance[current_node] = distance_dict.pop(current_node)

        if current_node.value == end_node.value:
            return shortest_distance[current_node], path

        for edge in current_node.edges:
            if edge.node in distance_dict:

                distance_to_neighbour = node_distance + edge.distance
                if distance_dict[edge.node] > distance_to_neighbour:
                    distance_dict[edge.node] = distance_to_neighbour


def shortest_path(M, start, goal):
    print("shortest path called here")
    node_list = []
    for intersection in M.intersections.keys():
        # print(intersection)
        node = GraphNode(intersection)
        node_list.append(node)

    graph = Graph(node_list)

    # add_edge() function will add a road from node1 to node2 (just 1 direction)
    for edge1, nearby_edges in enumerate(M.roads):
        # print(edge1, nearby_edges)
        edge1_x = M.intersections[edge1][0]
        edge1_y = M.intersections[edge1][1]
        # print(edge1_x, edge1_y)
        for edge2 in nearby_edges:
            # calculate the distance
            edge2_x = M.intersections[edge2][0]
            edge2_y = M.intersections[edge2][1]
            # print(edge2_x, edge2_y)
            distance = math.sqrt(pow(edge2_x - edge1_x, 2) + pow(edge2_y - edge1_y, 2))
            # print(distance)
            graph.add_road(node_list[edge1], node_list[edge2], distance)

    if start == goal:
        shortest_path_dict = {goal: 0}
    else:
        shortest_path_dict = uniform_cost_search(graph, node_list[start], node_list[goal],
                                                 tracking_route=TrackingRoutes(start))

    if shortest_path_dict is None:
        print(f'There is no road between {start} and {goal}')
    else:
        print(f'The shortest path from {start} to {goal} is {shortest_path_dict}')

    return



if __name__ == '__main__':
    map_10_intersections = {0: [0.7798606835438107, 0.6922727646627362],
                            1: [0.7647837074641568, 0.3252670836724646],
                            2: [0.7155217893995438, 0.20026498027300055],
                            3: [0.7076566826610747, 0.3278339270610988],
                            4: [0.8325506249953353, 0.02310946309985762],
                            5: [0.49016747075266875, 0.5464878695400415],
                            6: [0.8820353070895344, 0.6791919587749445],
                            7: [0.46247219371675075, 0.6258061621642713],
                            8: [0.11622158839385677, 0.11236327488812581],
                            9: [0.1285377678230034, 0.3285840695698353]}
    map_10_roads = [[7, 6, 5], [4, 3, 2], [4, 3, 1], [5, 4, 1, 2], [1, 2, 3],
                    [7, 0, 3], [0], [0, 5], [9], [8]]
    map_10 = Map(map_10_intersections, map_10_roads)

    # shortest_path(map_10, 0, 0)
    # shortest_path(map_10, 8, 9)
    # shortest_path(map_10, 0, 6)
    # shortest_path(map_10, 0, 7)
    # shortest_path(map_10, 0, 5)
    # shortest_path(map_10, 0, 3)
    # shortest_path(map_10, 0, 1)
    # shortest_path(map_10, 0, 2)
    shortest_path(map_10, 0, 4)
    # shortest_path(map_10, 0, 8)

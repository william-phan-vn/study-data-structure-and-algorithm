''' Uniform Cost Search - Cheapest First Search '''

import math


class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []
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


class Map:
    def __init__(self, intersections, roads):
        self.intersections = intersections
        self.roads = roads


# def uniform_cost_search(graph: Graph, start_node, end_node, distance_dict={}, shortest_distance=0, shortest_path={}):
def uniform_cost_search(graph: Graph, start_node, end_node, shortest_path, path_cost_dict={}):
    '''

    Args:
        graph:
        start_node:
        end_node:
        distance_dict: a dictionary that stores the distance to edge nodes wrt the start_node in the form of node:distance as key:value
        shortest_distance: the shortest distance road between start_node and end_node
        shortest_path: the shortest path from start node to end node

    Returns:
        shortest_distance, shortest_path
    '''

    '''Starting exploring the space'''

    # Set the start_node in the graph as explored
    graph.nodes[start_node.value].explored = True

    # Remove the last edge from the shortest path if there's no edge
    if len(start_node.edges) <= 1:
        shortest_path.pop(start_node.value)

    # Go through the Frontier path and Define the path_cost_list
    for edge in start_node.edges:
        if not graph.nodes[edge.node.value].explored:
            path_cost_dict[edge.node] = edge.distance

    # If the path_cost_dict is empty: There's no road between 2 city
    if len(path_cost_dict) == 0:
        return None

    # Short the path cost to find the min cost
    current_node, node_distance = sorted(path_cost_dict.items(), key=lambda x: x[1])[0]

    # Add the current node to the shortest_path
    shortest_path[current_node.value] = node_distance

    # Check if the current_node is the end_node
    if current_node.value == end_node.value:
        return shortest_path
    # Remove the cheapest path cost from the dict, because it will be explored in the next step
    path_cost_dict.pop(current_node)

    # Go through the cheapest cost path, repeat the uniform cost search
    return uniform_cost_search(graph, current_node, end_node, shortest_path, path_cost_dict)

    # for edge in start_node.edges:
    #     if graph.nodes[edge.node.value].seen:
    #         continue
    #     if distance_dict.get(edge.node) is None:
    #         distance_dict[edge.node] = shortest_distance + edge.distance
    #     else:
    #         shortest_path.pop(start_node.value)
    #
    # # Sort the distance_dict
    # distance_list = sorted(distance_dict.items(), key=lambda x: x[1])
    #
    # for index, item in enumerate(distance_list):
    #     current_node = item[0]
    #     distance = item[1]
    #
    #     shortest_distance = distance
    #     shortest_path[current_node.value] = shortest_distance
    #
    #     if current_node.value == end_node.value:
    #         return shortest_distance, shortest_path
    #
    #     distance_dict.pop(current_node)
    #     if len(current_node.edges) > 1:
    #         return uniform_cost_search(graph, current_node, end_node, distance_dict, shortest_distance, shortest_path)
    #     else:
    #         shortest_path.pop(current_node.value)
    #         graph.nodes[current_node.value].seen = True


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
                                                 shortest_path={start: 0})

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

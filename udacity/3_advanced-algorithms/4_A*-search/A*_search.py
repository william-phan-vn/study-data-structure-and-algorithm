''' A* Search - Best estimated total path cost first Search'''

import math
from typing import List, Dict


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance


class GraphNode(object):
    def __init__(self, val, coordinate: Coordinate):
        self.value = val
        self.coordinate = coordinate
        self.edges = []
        self.is_frontier = False
        self.explored = False

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_road(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)


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


def get_distance(p1: Coordinate, p2: Coordinate) -> float:
    return math.sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))


def a_star_search(start_node, end_node):
    # Define the frontier_nodes and explored_nodes
    frontier_nodes = ([start_node])
    explored_nodes = ([])

    # Define the distance_dict wrf the start node
    distance_dict = {start_node: 0}

    # Define the path that keep track of the previous node that can lead to the current node
    path_tracking = {start_node: start_node}

    while len(frontier_nodes) > 0:
        current_node = None

        for node in frontier_nodes:
            if current_node is None:
                current_node = node

            current_estimated_distance = distance_dict[current_node] \
                                         + get_distance(current_node.coordinate, end_node.coordinate)
            if distance_dict[node] + get_distance(node.coordinate, end_node.coordinate) \
                    < current_estimated_distance:
                current_node = node

        if current_node is None:
            return None

        if current_node == end_node:
            found_path = []

            # Trace back through the path tracking to get the shortest path
            while path_tracking[current_node] != current_node:
                found_path.append(current_node.value)
                current_node = path_tracking[current_node]

            found_path.append(start_node.value)
            found_path.reverse()
            return found_path

        # Go through the current node edges:
        for edge in current_node.edges:
            # Add unexplored nodes to the frontier
            edge_distance = distance_dict[current_node] + edge.distance
            if edge.node not in frontier_nodes \
                and edge.node not in explored_nodes:
                frontier_nodes.append(edge.node)
                path_tracking[edge.node] = current_node
                distance_dict[edge.node] = edge_distance
            else:
                # This edge is explored or in the frontier (means that there's a route go through this edge node already)
                # --> check if it's faster if we go through this new route
                # (from the current node to this edge node) instead of the edge current route
                # if yes --> change the distance and route tracking
                if distance_dict[edge.node] > edge_distance:
                    distance_dict[edge.node] = edge_distance
                    path_tracking[edge.node] = current_node

                    # If this edge node was explored --> move it back to the frontier
                    if edge.node in explored_nodes:
                        explored_nodes.remove(edge.node)
                        frontier_nodes.append(edge.node)

        # After all, the node has been explored
        frontier_nodes.remove(current_node)
        explored_nodes.append(current_node)

    # There's no frontier node left, means that there no route between to places
    return None


def shortest_path(M, start, goal):
    print("shortest path called here")
    node_list = []
    for intersection, coordinates in M.intersections.items():
        node = GraphNode(intersection, Coordinate(coordinates[0], coordinates[1]))
        node_list.append(node)

    graph = Graph(node_list)

    # add_edge() function will add a road from node1 to node2 (just 1 direction)
    for edge1, nearby_edges in enumerate(M.roads):
        # print(edge1, nearby_edges)
        coordinates_1 = Coordinate(M.intersections[edge1][0],
                                   M.intersections[edge1][1])
        # print(edge1_x, edge1_y)
        for edge2 in nearby_edges:
            # calculate the distance
            coordinates_2 = Coordinate(M.intersections[edge2][0],
                                     M.intersections[edge2][1])
            # print(edge2_x, edge2_y)
            distance = get_distance(coordinates_1, coordinates_2)
            # print(distance)
            graph.add_road(node_list[edge1], node_list[edge2], distance)

    if start == goal:
        shortest_route = [goal]
    else:
        shortest_route = a_star_search(node_list[start], node_list[goal])

    if shortest_route is None:
        print(f'There is no road between {start} and {goal}')
    else:
        print(f'The shortest path from {start} to {goal} is {shortest_route}')

    return shortest_route


MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]


if __name__ == '__main__':
    map_40_intersections = {0: [0.7801603911549438, 0.49474860768712914],
                            1: [0.5249831588690298, 0.14953665513987202],
                            2: [0.8085335344099086, 0.7696330846542071],
                            3: [0.2599134798656856, 0.14485659826020547],
                            4: [0.7353838928272886, 0.8089961609345658],
                            5: [0.09088671576431506, 0.7222846879290787],
                            6: [0.313999018186756, 0.01876171413125327],
                            7: [0.6824813442515916, 0.8016111783687677],
                            8: [0.20128789391122526, 0.43196344222361227],
                            9: [0.8551947714242674, 0.9011339078096633],
                            10: [0.7581736589784409, 0.24026772497187532],
                            11: [0.25311953895059136, 0.10321622277398101],
                            12: [0.4813859169876731, 0.5006237737207431],
                            13: [0.9112422509614865, 0.1839028760606296],
                            14: [0.04580558670435442, 0.5886703168399895],
                            15: [0.4582523173083307, 0.1735506267461867],
                            16: [0.12939557977525573, 0.690016328140396],
                            17: [0.607698913404794, 0.362322730884702],
                            18: [0.719569201584275, 0.13985272363426526],
                            19: [0.8860336256842246, 0.891868301175821],
                            20: [0.4238357358399233, 0.026771817842421997],
                            21: [0.8252497121120052, 0.9532681441921305],
                            22: [0.47415009287034726, 0.7353428557575755],
                            23: [0.26253385360950576, 0.9768234503830939],
                            24: [0.9363713903322148, 0.13022993020357043],
                            25: [0.6243437191127235, 0.21665962402659544],
                            26: [0.5572917679006295, 0.2083567880838434],
                            27: [0.7482655725962591, 0.12631654071213483],
                            28: [0.6435799740880603, 0.5488515965193208],
                            29: [0.34509802713919313, 0.8800306496459869],
                            30: [0.021423673670808885, 0.4666482714834408],
                            31: [0.640952694324525, 0.3232711412508066],
                            32: [0.17440205342790494, 0.9528527425842739],
                            33: [0.1332965908314021, 0.3996510641743197],
                            34: [0.583993110207876, 0.42704536740474663],
                            35: [0.3073865727705063, 0.09186645974288632],
                            36: [0.740625863119245, 0.68128520136847],
                            37: [0.3345284735051981, 0.6569436279895382],
                            38: [0.17972981733780147, 0.999395685828547],
                            39: [0.6315322816286787, 0.7311657634689946]}
    map_40_roads = [[36, 34, 31, 28, 17],
                    [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
                    [39, 36, 21, 19, 9, 7, 4], [35, 20, 15, 11, 6],
                    [39, 36, 21, 19, 9, 7, 2], [32, 16, 14],
                    [35, 20, 15, 11, 1, 3], [39, 36, 22, 21, 19, 9, 2, 4],
                    [33, 30, 14], [36, 21, 19, 2, 4, 7],
                    [31, 27, 26, 25, 24, 18, 17, 13], [35, 20, 15, 3, 6],
                    [37, 34, 31, 28, 22, 17], [27, 24, 18, 10],
                    [33, 30, 16, 5, 8], [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
                    [37, 30, 5, 14],
                    [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
                    [31, 27, 26, 25, 24, 1, 10, 13, 17], [21, 2, 4, 7, 9],
                    [35, 26, 1, 3, 6, 11, 15], [2, 4, 7, 9, 19],
                    [39, 37, 29, 7, 12], [38, 32, 29], [27, 10, 13, 18],
                    [34, 31, 27, 26, 1, 10, 15, 17, 18],
                    [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
                    [31, 1, 10, 13, 18, 24, 25, 26],
                    [39, 36, 34, 31, 0, 12, 17], [38, 37, 32, 22, 23],
                    [33, 8, 14, 16],
                    [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
                    [38, 5, 23, 29], [8, 14, 30], [0, 12, 17, 25, 26, 28, 31],
                    [1, 3, 6, 11, 15, 20], [39, 0, 2, 4, 7, 9, 28],
                    [12, 16, 22, 29], [23, 29, 32], [2, 4, 7, 22, 28, 36]]
    map_40 = Map(map_40_intersections, map_40_roads)

    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start,
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")

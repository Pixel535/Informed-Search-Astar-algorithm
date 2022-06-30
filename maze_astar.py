import math
from collections import deque
from operator import attrgetter
import maze_puzzle as mp


# Function to find a route using A* Search algorithm.

# The A* algorithm usually improves performance by estimating heuristics to minimize cost of the next node visited.
# Total cost is calculated using two metrics: the total distance from the start node to the current node, and the
# estimated cost of moving to a specific node by utilizing a heuristic. When attempting to minimize cost, a lower
# value will indicate a better performing solution.
def run_astar(maze_game, root_point, visited_points):
    # TODO: Dla podstawowej postaci labiryntu wynik powinien być identyczny jak w BFS.
    stack = deque()
    stack.append(root_point)
    while stack:
        current_point = stack.popleft()
        if not is_in_visited_points(current_point, visited_points):
            visited_points.append(current_point)
            if maze_game.get_current_point_value(current_point) == '*':
                return current_point
            else:
                neighbors = maze_game.get_neighbors(current_point)
                for neighbor in neighbors:
                    neighbor.set_parent(current_point)
                    neighbor.set_cost(determine_cost(current_point, neighbor))
                    stack.append(neighbor)
                stack = deque(sorted(stack, key=attrgetter('cost')))
    return False


# Determine cost based on the distance to root
def determine_cost(origin, target):
    # TODO
    distance_to_root = math.hypot(origin.x-target.x, origin.y-target.y)
    cost_to_move = mp.get_move_cost(origin, target)
    return (distance_to_root + cost_to_move)


# Function to determine if the point has already been visited
def is_in_visited_points(current_point, visited_points):
    for visited_point in visited_points:
        if current_point.x == visited_point.x and current_point.y == visited_point.y:
            return True
    return False


def start_astar(maze_game_main, x, y):
    print('---A* Search---')

    # Function to determine if the point has already been visited
    starting_point = mp.Point(x - 1, y - 1)
    # Run the greedy search algorithm with the initialized maze
    outcome = run_astar(maze_game_main, starting_point, [])

    # Get the path found by the greedy search algorithm
    if not run_astar(maze_game_main, starting_point, []):
        print("\n-----No path to the goal found.-----\n")
    else:
        print("\n-----WYNIK-----\n")
        astar_path = mp.get_path(outcome)

        # Print the results of the path found
        print('PATH LENGTH: ', mp.get_path_length(outcome))
        maze_game_main.overlay_points_on_map(astar_path)
        print('PATH COST: ', mp.get_path_cost(outcome))
        for point in astar_path:
            print('Point: ', point.x, ',', point.y)

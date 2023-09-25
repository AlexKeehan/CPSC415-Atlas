#!/usr/bin/env python3
'''
CPSC 415 -- Homework #2 template
Alexander Keehan, University of Mary Washington, Fall 2023
'''
import sys
from atlas import Atlas


def find_path(atlas, alg):
    '''Finds a path from src to dest using a specified algorithm, and
    based on costs from the atlas provided. The second argument must be one
    of the values "greedy", "Dijkstras", or "A*".

    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.'''
   # THIS IS WHERE YOUR AMAZING CODE GOES
    if alg == "greedy":
        # Frontier stores the priority queue of nodes to go to next
        frontier = []
        # Visited stores the path taken to goal
        visited = []
        # neighbors stores the neighbors of an expanded node
        neighbors = []
        # Used to check if a node is used later on
        total_neighbors = []
        # Assign a node all their neighbors to check if they are used in the final path
        neighbors_for_nodes = []

        frontier.append(0)
        # sort stores the sorted list that is used to populate the frontier
        sort = []
        # node is the node being expanded
        node = 0
        flag = 0
        # Keep going until goal state is found
        while node != atlas._num_cities - 1:
            flag = 0
            # Reseat sort and neighbors every round
            sort = []
            # Store neighbors in total_neighbors
            total_neighbors.append(neighbors)
            neighbors = []

            node = frontier.pop(0)
        
            counter = 0
            # Get neighbors for node being expanded
            while counter < atlas._num_cities:
                dist = Atlas.get_road_dist(atlas, node, counter)
                if dist != float('Inf') and counter not in visited and counter != node:
                    neighbors.append(counter)
                counter = counter + 1
            neighbors_for_nodes.append([node, neighbors])

            # Organize neighbors based on heuristic
            for i in neighbors:
                dist = Atlas.get_crow_flies_dist(atlas, atlas._num_cities - 1, i)
                sort.append([i, dist])
            # Add values from frontier back in to be sorted again
            for i in frontier:
                dist = Atlas.get_crow_flies_dist(atlas, atlas._num_cities - 1, i)
                if [i, dist] not in sort:
                    sort.append([i, dist])
            # Sort all the neighbors and frontier by heuristic
            sort.sort(key = lambda x: x[1])
        
            # Check to see if there are any new neighbors
            for x in total_neighbors:
                for y in neighbors:
                    if y not in total_neighbors:
                        flag = 0
                        break;
                    else:
                        flag = 1

            # Add node to path
            if len(neighbors) != 0 and node not in visited and flag != 1:
                visited.append(node)
    
            # Reset frontier
            frontier = []

            # Add new sorted values to frontier
            for i in sort:
                if i[0] not in frontier:
                    frontier.append(i[0])

            # Check for goal state
            if len(sort) > 0:
                if sort[0][1] == 0.0:
                    break;

        temporary = []
        # Check for unused nodes in visited
        # Look for a nodes neighbors that are not being used by any other node in visited
        # Indicates it should not be on the final path
        for x in neighbors_for_nodes:
            for y in visited:
                if (y in x[1] and x[0] not in temporary) or atlas._num_cities - 1 in x[1] and x[0] not in temporary:
                    temporary.append(x[0])
    
        visited = temporary
        visited.append(atlas._num_cities - 1)
        next_node = 1
        curr_node = 0

        # Check for infinite values in visited
        while next_node < len(visited):
            dist = Atlas.get_road_dist(atlas, visited[curr_node], visited[next_node])
            if dist == float('Inf'):
                del visited[curr_node]
            curr_node = curr_node + 1
            next_node = next_node + 1
        # Add up the cost of visited to get the final cost
        next_node = 1
        curr_node = 0
        cost = 0
        while next_node < len(visited):
            dist = Atlas.get_road_dist(atlas, visited[curr_node], visited[next_node])
            cost = cost + dist
            curr_node = curr_node + 1
            next_node = next_node + 1
        return (visited, cost)
    elif alg == "Dijkstras":
        return "Unimplemented"
    elif alg == "A*":
        return "Unimplemented"

if __name__ == '__main__':
#
    if len(sys.argv) != 3:
        print("Usage: gps.py numCities|atlasFile algorithm.")
        sys.exit(1)

    if len(sys.argv) > 2:
        if sys.argv[2] not in ['greedy', 'Dijkstras', 'A*']:
            print(f'Algorithm must be one of: "greedy", "Dijkstras", or "A*".'
                f' (You put "{sys.argv[2]}".)')
            sys.exit(2)
        else:
            alg = sys.argv[2]

    try:
        num_cities = int(sys.argv[1])
        print(f'Building random atlas with {num_cities} cities...')
        usa = Atlas(num_cities)
        print('...built.')
    except:
        print(f'Loading atlas from file {sys.argv[1]}')
        usa = Atlas.from_filename(sys.argv[1])
        print('...loaded.')

    path, cost = find_path(usa, alg)
    print(f'The {alg} path from 0 to {usa.get_num_cities()-1}'
        f' costs {cost}: {path}.')
    ne = usa._nodes_expanded
    print(f'It expanded {len(ne)} nodes: {ne}')


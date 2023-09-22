#!/usr/bin/env python3

'''
CPSC 415 -- Homework #2 template
Alexander Keehan, University of Mary Washington, Fall 2023
'''

from atlas import Atlas
import numpy as np
import sys


def find_path(atlas, alg):
    '''Finds a path from src to dest using a specified algorithm, and
    based on costs from the atlas provided. The second argument must be one
    of the values "greedy", "Dijkstras", or "A*".

    Returns a tuple of two elements. The first is a list of city numbers,
    starting with 0 and ending with atlas.num_cities-1, that gives the
    optimal path between those two cities. The second is the total cost
    of that path.'''
   # THIS IS WHERE YOUR AMAZING CODE GOES

    queue = []
    grid = []

    def isEmpty(self):
        if len(queue) == 0:
            return True
        else:
            return False

    def delete(self):
        index = 0
        max_value = 100000
        for i in range(len(queue)):
            if queue[i] < max_value:
                max_value = queue[i]
                index = i
        temp = queue[index]
        del queue[index]
        return temp

    
    
    def Grid(self):
        x = 0
        y = 0
        while x <= atlas._num_cities - 1:
            y = 0
            while y <= atlas._num_cities - 1:
                grid.append([[x,y], Atlas.get_road_dist(atlas, x, y)])
                y = y + 1
            x = x + 1
    if (alg == "Dijkstras"):
        x = 0
        y = 0
        reached = [[]]
        frontier = []

        Grid(grid)

        print(grid)
        print(queue)

        node = [0,0]
        frontier.append(node)
        reached.append(node)
        queue.append(grid[0][3])
        while not len(frontier) == 0:
            frontier.pop()
            while y < atlas._num_cities:
                print(y)
                print(queue)
                queue.append(grid[x][y])
                y = y + 1
            
        print("Queue ", queue)


    # Here's a (bogus) example return value:
    return ([0,3,2,4],970)



if __name__ == '__main__':

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


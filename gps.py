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
    def MinDist(self, grid, completed):
        min = ([float('inf')])
        for x in range(len(grid) - 1):
            if grid[x] < min and completed[x] == False:
                min = grid[x]
                min_index = x
        return min_index

    if (alg == "Dijkstras"):
        x = 0
        y = 0
        grid = []
        numgrid = []
        state = [[]]
        completed = [[]]
        shortest = float('inf')
        ans_state = -1
        ans = []

        while x <= atlas._num_cities - 1:
            y = 0
            while y <= atlas._num_cities - 1:
                grid.append([Atlas.get_road_dist(atlas, x, y)])
                numgrid.append([x, y])
                y = y + 1
            x = x + 1
        state = [0,0]
        x = 0
        y = 0

        
        
        while state[0] != atlas._num_cities:
            while x <= atlas._num_cities - 1:
                y = 0
                while y <= atlas._num_cities - 1:
                    print(MinDist(atlas, grid, completed))
                    
                    y = y + 1
                ans.append(shortest)
                x = x + 1
            state[0] = atlas._num_cities
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


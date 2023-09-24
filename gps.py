#!/usr/bin/env python3
import heapq
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

    frontier = []
    grid = []
    backtrack = []

    def Grid(self):
        x = 0
        y = 0
        if (alg == "Dijkstras"):
            while x <= atlas._num_cities - 1:
                y = 0
                while y <= atlas._num_cities - 1:
                    grid.append([[x,y], Atlas.get_road_dist(atlas, x, y)])
                    y = y + 1
                x = x + 1

        if (alg == "greedy"):
            while x <= atlas._num_cities - 1:
                y = 0
                while y <= atlas._num_cities - 1:
                    if Atlas.get_road_dist(atlas, x, y) != float('Inf') and Atlas.get_road_dist(atlas, x, y) != 0.0:
                        grid.append([[x,y], Atlas.get_crow_flies_dist(atlas, x, y)])
                    y = y + 1
                x = x + 1
        if (alg == "A*"):
            while x <= atlas._num_cities - 1:
                y = 0
                while y <= atlas._num_cities - 1:
                    temp = Atlas.get_road_dist(atlas, x, y) + Atlas.get_crow_flies_dist(atlas, x, y)
                    grid.append([[x,y], temp])
                    y = y + 1
                x = x + 1
    Grid(grid)


    if (alg == "greedy"):
        #print("Hueristic", Atlas.get_crow_flies_dist(atlas, grid[22][0][0], grid[22][0][1]))
        tempgrid = []
        for i in grid:
            opposite = [i[0][1], i[0][0]]
            for p in grid:
                if p[0] == opposite:
                    backtrack.append(p)
                    grid.remove(p)
        print("Grid", grid)
        print("Backtrack", backtrack)
        #print("Actual", Atlas.get_road_dist(atlas, grid[36][0][0], grid[36][0][1]))
        queue = []
        
        queue = []
        pos = 0
        
        ans = []
        cost = 0
        previous_move = []
        visited = [[0,0]]
        potential_moves = []
        first = 0
        prev = []
        back = []
        rev = []
        while pos != atlas._num_cities - 1:
            i = 0
            # Sorting
            while i < len(grid):
                if grid[i][0][0] == pos and grid[i][0][0] not in visited:
                    queue.append(grid[i])
                i = i + 1
            queue.sort(key = lambda x: x[1])
            counter = 0

            print("Queue", queue)
            #print("Prev", prev)
            #print("TEST", [queue[0][0][0], queue[0][0][1]])
            
            if [queue[0][0][0], queue[0][0][1]] not in visited:
                pos = queue[0][0][1]
            print(pos)

            x1 = visited[len(visited) - 1][0]
            y1 = visited[len(visited) - 1][1]
            x2 = visited[len(visited) - 2][0]
            y2 = visited[len(visited) - 2][1]
            x = [x1, y1]
            y = [y2, x2]
            if x != y:
                cost = cost + queue[0][1]
                ans.append(queue[0])
            else:
                back = y
            if [queue[0][0][0], queue[0][0][1]] not in visited:
                visited.append([queue[0][0][0], queue[0][0][1]])
            #print("Visited", visited)
            prev = queue
            queue = []
    
        temp = []
        for i in ans:
            if i[0][0] not in temp:
                temp.append(i[0][0])
            if i[0][1] not in temp:
                temp.append(i[0][1])
        ans = temp
        return (ans, cost)

    # Here's a (bogus) example return value:
    #return ([0,3,2,4],970)



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


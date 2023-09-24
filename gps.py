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
    print(grid)


    if (alg == "greedy"):
        #print("Hueristic", Atlas.get_crow_flies_dist(atlas, grid[22][0][0], grid[22][0][1]))

        #print("Actual", Atlas.get_road_dist(atlas, grid[36][0][0], grid[36][0][1]))
        queue = []

        queue = []
        pos = 0
        ans = []
        cost = 0
        previous_move = []
        visited = [[0,0]]
        first = 0
        while pos != atlas._num_cities - 1:
            i = 1
            # Sorting
            while i < atlas._num_cities:
                queue.append([[pos,i], grid[i][1]])
                i = i + 1
            queue.sort(key = lambda x: x[1])
            counter = 0
            temp_queue = []
            # Finding ones that aren't Inf
            while counter < len(queue):
                #print("Queue", queue)
                #print("TEST", queue[0][1])
                dist = Atlas.get_road_dist(atlas, queue[counter][0][0], queue[counter][0][1])
                index = [queue[counter][0][0], queue[counter][0][1]]
                if dist != float('Inf') and dist != 0.0 and index not in visited:
                    #print("Dist", dist)
                    temp_queue.append([queue[counter][0], dist])
                    #print(temp_queue)
                counter = counter + 1
            queue = temp_queue
            queue.sort(key = lambda x: x[1])
            #print("Sorted Queue", queue)
            
            if queue[0][0][1] not in visited:
                pos = queue[0][0][1]
            x1 = visited[len(visited) - 1][0]
            y1 = visited[len(visited) - 1][1]
            x2 = visited[len(visited) - 2][0]
            y2 = visited[len(visited) - 2][1]
            x = [x1, y1]
            y = [y2, x2]
            if x != y:
                cost = cost + queue[0][1]
                ans.append(queue[0])
            visited.append([queue[0][0][0], queue[0][0][1]])
            #print("Visited", visited)
            first = 1
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


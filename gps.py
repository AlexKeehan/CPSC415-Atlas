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
        
        
        for i in grid:
            opposite = [i[0][1], i[0][0]]
            for p in grid:
                if p[0] == opposite:
                    backtrack.append(p)
                    grid.remove(p)
        print("Grid", grid)
        print("Backtrack", backtrack)
        
        
        queue = grid
        pos = 0
        ans = []
        cost = 0
        previous_move = []
        visited = [[0,0]]
        potential_moves = []
        reached = [0]
        last_pos = 0
        reached_queue = []
        # Keep going until goal state
        while pos != atlas._num_cities - 1:
            potential_moves = []
            
            i = 0
            # Sorting frontier
            while i < len(queue):
                if queue[i][0][0] in reached and queue[i][0] not in visited:
                    potential_moves.append(queue[i])
                i = i + 1
            if potential_moves == []:
                print("Backtrack")
                pos = last_pos
                queue.pop(0)
            potential_moves.sort(key = lambda x: x[1])
            queue.sort(key = lambda x: x[1])
            print("Queue", queue)
            print("Potential moves", potential_moves)
            
            #print("TEST", [queue[0][0][0], queue[0][0][1]])
            print("pos before", last_pos)
            next_pos = potential_moves[0][0][0]
            for i in potential_moves:
                
                if i[0][0] in reached:
                    pos = potential_moves[0][0][1]
                    last_pos = potential_moves[0][0][0]
                    if pos not in reached:
                        reached.append(pos)
            print("Reached", reached)
            print("Pos", pos)

            cost = cost + potential_moves[0][1]
            ans.append(potential_moves[0])
            
            if [potential_moves[0][0][0], potential_moves[0][0][1]] not in visited:
                visited.append([potential_moves[0][0][0], potential_moves[0][0][1]])
            #print("Visited", visited)
            
    
        temp = []
        for i in ans:
            if i[0][0] not in temp:
                temp.append(i[0][0])
            if i[0][1] not in temp:
                temp.append(i[0][1])
        ans = temp
        #print("ANS", ans)
        return (ans, cost)

    # Here's a (bogus) example return value:
    #return ([0,3,2,4],970)



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


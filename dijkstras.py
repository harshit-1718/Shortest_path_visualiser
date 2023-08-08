import math
import pygame
from queue import PriorityQueue

HEIGHT, WIDTH = 800, 800


def reconstructPath(came_from, current, draw):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            draw()


def dijkstra(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
   

    # open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        # open_set_hash.remove(current)
        

        if current == end:
            reconstructPath(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
               
                # if neighbor not in open_set_hash:
                count += 1
                open_set.put((g_score[neighbor], count, neighbor))
                #open_set_hash.add(neighbor)
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
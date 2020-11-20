#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from parse_map import parse_map


def _is_obstacle(p):
    return bool(p)


def _has_obstacle(m):
    for x in range(len(m[0])-1, -1, -1):
        for y in range(len(m)-1, -1, -1):
            if _is_obstacle(m[y][x]):
                return True
            else:
                continue
    return False


def _get_square_matrix(M, x, y, size):
    """Extract square part with a side of size of matrix M from (x,y) point"""
    return [[M[i][j] for j in range(x, x+size)] for i in range(y,y+size)]


def _get_max_size(x, y, map_info):
    """
    Get the size of the biggest square matrix in the map
    with first point: (x, y)
    
    Arguments:
    x -- column index
    y -- line index
    map_info -- a dict of the map and its information
    
    Returns:
    size -- biggest square matrix size
    """
    x_max = map_info["line_len"]
    y_max = map_info["line_num"]
    return min(x_max-x, y_max-y)


def _find_square(map_info):
    """
    Get the coordinates of the top left point and the size 
    of the larger square included in the map with no obstacles.
    If many of this same size exit, get the top left one.
    
    Arguments:
    map_info -- a dict of the map and its information
    
    Returns:
    x_square -- column index of square's top left point
    y_square -- line index of square's top left point
    max_size -- square's size
    """
    x_square, y_square, size = 0, 0, 0
    for y in range(map_info["line_num"]):
        for x in range(map_info["line_len"]):
            max_size = _get_max_size(x, y, map_info)
            if max_size > size:
                for s in range(max_size, size, -1):
                    m = _get_square_matrix(map_info["matrix"], x, y, s)
                    if _has_obstacle(m):
                        continue
                    else:
                        print(f"({x},{y}) max_size = {max_size} ; size =  = {size} ; s = {s}")
                        size = s
                        x_square = x
                        y_square = y
                        break
            else:
                continue
    return x_square, y_square, size


def print_map_with_square(map, x, y, size):
    pass


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print('Missing file path.')
    #     exit()
    map = parse_map("./map_file")
    x, y, size = _find_square(map)
    print(x, y, size)
    # print_map_with_square(map, x, y, size)
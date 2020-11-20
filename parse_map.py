#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class MapError(Exception):
    pass


def _parse_first_line(f):
    """
    Parse map first line.
    
    Arguments:
    f -- opened file object pointing at the top
    
    Returns:
    f -- opened file object pointing at the second line
    line_num -- number of line in the map
    empty -- empty character in the map
    obstacle -- obstacle character in the map
    full -- full character in the map
    """
    first_line = f.readline()
    i = 0
    c = first_line[i]
    line_num = ""
    while c in "0123456789":
        line_num+=c
        i+=1
        c = first_line[i]
    line_num = int(line_num)
    empty = c
    obstacle = first_line[i+1]
    full = first_line[i+2]
    if first_line[i+3] != "\n":
        raise MapError("map has more lines that indicated on file's first line")
    return f, line_num, empty, obstacle, full


def _parse_line(string, empty, obstacle):
    """
    Parse a string of characters, returns a list of booleans:
    True for empty and False for obstacles
    """
    line = []
    for c in string:
        if c == empty:
            line.append(False)
        elif c == obstacle:
            line.append(True)
        else:
            raise MapError("char is not neither an empty or an obstacle char")
    return line


def _parse_matrix(line_num, empty, obstacle, f):
    """
    Parse map contain in a file.
    
    Arguments:
    line_num -- number of lines in map
    empty -- empty character of map
    obstacle -- obastacle character of map
    file -- line_num remaining lines of the file
    
    Returns:
    M -- boolean matrix of empty (True) and obstacle (False) chars in map
    """ 
    M = []
    first_line = f.readline()[:-1] # remove '\n' char at end of line
    line_len = len(first_line)
    M.append(_parse_line(first_line, empty, obstacle))
    for _ in range (1, line_num):
        line = f.readline()[:-1] # remove '\n' char at end of line
        if len(line) != line_len:
            raise MapError("map lines does not all have the same length")
        M.append(_parse_line(line, empty, obstacle))
    if f.read(1):
        raise MapError("map has more lines that indicated in first line of the file")
    return M, line_len


def parse_map(path):
    """
    Parse map contained in a file.
    
    Arguments:
    path -- path to the file on system
    
    Returns:
    parameters -- a dictionary containing line number, empty, obstacle and full char and matrix
    """
    f = open(path, "r")
    f, line_num, empty, obstacle, full = _parse_first_line(f)
    M, line_len = _parse_matrix(line_num, empty, obstacle, f)
    f.close()
    return {
        "line_len": line_len,
        "line_num": line_num,
        "empty_char": empty,
        "obstacle_char": obstacle,
        "full_char": full,
        "matrix": M
    }


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing file path.')
        exit()
    print(parse_map(sys.argv[1]))

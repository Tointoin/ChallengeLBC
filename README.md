# Challenge LBC

> :warning: This is an **alpha version**.

This project aims to meet LBC's backend development challenge summerized in joined pdf file.

This project is built with Python 3 standard library.

## Commands


To generate a `map_file` with a map of:
* 9 lines
* 27 columns
* density of 1

```
$ python map_gen.py 27 9 1 > map_file
```

To visualize its content (notice that first line indicates information about the map):

```
$ cat map_file
9.ox
.....o.....................
o......o.....o.........o...
....................oo.....
...........o........o......
.o....o............o.......
...........................
.....oo...................o
..............o......o.....
..o....o.o..............o..
```

To visualize the map replacing `.` with `x` for the biggest square of the map (first top left if many):

```
$ python find_square.py map_file
.....o.....................
o......o.....o.........o...
............xxxxx...oo.....
...........oxxxxx...o......
.o....o.....xxxxx..o.......
............xxxxx..........
.....oo.....xxxxx.........o
..............o......o.....
..o....o.o..............o..
```
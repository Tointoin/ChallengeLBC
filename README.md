# Challenge LBC

This project aims to meet LBC's backend development challenge summerized in joined pdf file.

This project is built with Python 3 standard library.

## Map generation

To generate an `example_file` with a map of:
* 9 lines
* 27 columns
* density of 1

```
$ python map_gen.py 27 9 1 > map_file
```

## Map Visualization

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

## Map Visualization with square

To visualize the map replacing `.` with `x` for the biggest square of the map (first top left if many):

```
$ python find_square.py map_file
.....o........xxxxx........
o......o.....oxxxxx....o...
..............xxxxx.oo.....
...........o..xxxxx.o......
.o....o.......xxxxxo.......
...........................
.....oo...................o
..............o......o.....
..o....o.o..............o..
```

## Run tests

Tests files of maps are in `tests` folder with name `{myTestName}_test`. Corresponding expected outputs are in `test_results` folder with corresponding name: `{myTestName}_result`.

To check that every that every test leads to the right result:

```
python test.py
```

# esperGrid
A makeshift open-source module made for Python, about making grids made of ASCII

**You can find the code in `esperGrid.py`.**
The file organisation is really messy due to the way that Replit runs things.

The data is stored in a two dimensional list, which accounts for rows and columns.

You can access the grid's contents through `textgrid[(x,y)]`, or if you plan on doing more in-depth development, then it can be accessed through `textgrid.content[x][y]`.

You can set an item in the grid the same way you would with a dictionary:
`textgrid[(x,y)] = value`

The textgrid also comes with a variety of procedures which make the grid easier to deal with, such as `.replace()`, `.move()`, `.spread()`, `.set_many()`, and more.

The textgrid also comes with a convenient `.index()` function which returns a list of co-ordinates, corresponding to the position of value you're searching for in the grid.
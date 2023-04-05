# esperGrid
A makeshift open-source module made for Python, about making grids made of ASCII

The data is stored in a 2D list, with each list representing a column and then each item in that list representing a single cell.
The grid will automatically scale to the contents of the grid, unless a cell width is specified (which might not actually work now I'm thinking about it).
When entering co-ordinates, a format is followed consistently.

*When accessing the raw data array, access it the following syntax:*

  `textGrid.contents[ X-coordinate ][ Y-coordinate ]`
  
*When using built-in functions/procedures, using the format:*

  `[ X-coordinate , Y-coordinate ]`
  
*Use this format as your argument in the procedure or function you'd like to use*

For a list of all usable functions, classes, procedures, attributes, and any syntax you may find useful in the module, use the procedure: `eg.define(obj=None)`.
This will give you all attributes of the object specified through `obj`. When `obj = None`, the properties, attributes of the module itself are defined in terms of their syntax. No explanation is given to these, when they are being defined.

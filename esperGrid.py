
import random as rn

# EsperGrid v2.13.0

'''
A makeshift module by Aden L
Used to make grids in the form of strings printed in the terminal
Good for simple programs that need a simple grid UI
'''

############### GENERAL ###############

class textgrid:

  ## DUNDER ##
  
  def __init__(self, width=10, height=10, min_length=-1, placeholder=' ', column_gap=1):
    self.width = int(width)
    self.height = int(height)
    self.min_length = int(min_length)
    self.placeholder = placeholder
    self.column_gap = column_gap
    self.content = [[None for h in range(self.height)] for w in range(self.width)]

  def __repr__(self):
    return str(self.content)
  
  def __str__(self):
    output = ''
    max = self.find_max()
    for y in range(self.height-1, -1, -1):
      for x in range(self.width):
        if self.content[x][y] == None:
          output += '{0:<{w}}'.format(self.placeholder, w=max)
        else:
          output += '{0:<{w}}'.format(self.content[x][y], w=max)
        if x != self.width-1:
          output += ' '*self.column_gap
      if y != 0:
        output += '\n'
    return output

  def __getitem__(self, coord):
    return self.content[coord[0]][coord[1]]

  def __setitem__(self, coord, value):
    if value != None:
      value = str(value)
    self.content[coord[0]][coord[1]] = value

  def __contains__(self, item):
    for y in range(self.height):
      for x in range(self.width):
        if self.content[x][y] == item:
          return True
    return False

  ## FUNCTIONS ##

  def index(self, *args: str) -> list:
    output = []
    for y in range(self.height):
      for x in range(self.width):
        if self.content[x][y] in args:
          output.append((x,y))
    return output

  def find_max(self) -> int:
    max_length = self.min_length
    for y in range(self.height):
      for x in range(self.width):
        if self.content[x][y] == None:
          current_length = len(self.placeholder)
        else:
          current_length = len(self.content[x][y])
        if current_length > max_length:
          max_length = current_length
    return max_length

  ## METHODS ##

  def set_many(self, value, coords):
    for coord in coords:
      self[coord] = value

  def move(self, coord_a, coord_b, copy=False):
    self[coord_b] = self[coord_a]
    if not copy:
      self[coord_a] = None

  def swap(self, coord_a, coord_b):
    temp_a = self[coord_a]
    self[coord_a] = self[coord_b]
    self[coord_b] = temp_a

  def replace(self, value, new_value, limit =-1, random =True):
    coords = self.index(value)
    if len(coords) > limit > 0:
      if random:
        rn.shuffle(coords)
      coords = coords[:limit]
    self.set_many(new_value, coords)

  def spread(self, value, quantity =1):
    quantity = int(quantity)
    visited = []
    for i in range(quantity):
      coord = None
      while coord in visited or coord == None:
        coord = (rn.randint(0,self.width-1), 
                 rn.randint(0,self.height-1))
      visited.append(coord)
      self[coord] = value

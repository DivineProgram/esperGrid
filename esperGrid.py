
import random as rn
from math import sqrt

# EsperGrid v2.0

'''
A makeshift module by Aden L
Used to make grids in the form of strings printed in the terminal
Good fo simple programs that need a simple grid UI
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

    def __get__(self):
      pass

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

  def set(self, item, coord=(0,0)):
    item = str(item)
    self.content[coord[0]][coord[1]] = item

  def set_many(self, item, coords=[(0,0)]):
    for coord in coords:
      self.set(item, coord)

  def spread(self, item, quantity: int=1):
    quantity = int(quantity)
    for i in range(quantity):
      self.set(item,(rn.randint(0,self.width-1),
                   rn.randint(0,self.height-1)))

grid = textgrid(placeholder='.')
grid.spread('#', 3)
print(grid)

import random as rn
from math import sqrt

# EsperGrid v2.0

'''
A makeshift module by Aden L
Used to make grids in the form of strings printed in the terminal
Good fo simple programs that need a simple grid UI
'''

############### GENERAL ###############

class grid:
  
  def __init__(self, width=10, height=10, min_length=-1, placeholder=' '):
    self.width = int(width)
    self.height = int(height)
    self.min_length = int(min_length)
    self.placeholder = placeholder
    self.content = [[None for w in range(self.width)] for h in range(self.height)]
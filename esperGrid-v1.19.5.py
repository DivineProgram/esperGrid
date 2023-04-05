
import random as rn
from math import sqrt

# EsperGrid v1.19.5

'''
A makeshift module by Aden L
Used to make grids in the form of strings printed in the terminal
Good fo simple programs that need a simple grid UI
'''

############### GENERAL ###############

def define(obj=None):
  print('[ ----- ----- ----- ]')
  
  if obj == 'textGrid':
    print('textGrid.width')
    print('textGrid.height')
    print('textGrid.cellWidth')
    print('textGrid.borderSpace')
    print('textGrid.contents')
    print('  -  ')
    print('textGrid.__init__(self, defWidth=10, defHeight=10, defSlot=None, emptySlot=' ', cWidth=-1, space=1)')
    print('textGrid.__str__(self)')
    print('textGrid.checkCoords(self,coords)')
    print('textGrid.refresh(self)')
    print('textGrid.checkFormat(self)')
    print('textGrid.display(self)')
    print('textGrid.setSlot(self, coords, content=None)')
    print('textGrid.setRow(self, row, content=None)')
    print('textGrid.setColumn(self, column, content=None)')
    print('textGrid.setSpread(self, content=None, items=1, equalQuantities=False, overlap=False)')
    print('textGrid.setMove(self, coord, destination, duplicate=False)')
    print('textGrid.setSwap(self, coordA, coordB)')
    print('  -  ')
    print('textGrid.get(self, coords)')
    print('textGrid.formatWidth(self, data)')
    print('textGrid.search(self, content=None)')
  
  else:
    print('eg.textGrid')
    print('  -  ')
    print('eg.define(obj)')
    print('  -  ')
    print('eg.extract(data)')
    print('eg.len_extracted(data)')
    print('eg.magnitude(cordA=[0,0], cordB=[0,0])')
  
  print('[ ----- ----- ----- ]')

def extract(data): # Rid of leading spaces
  if data == None:
    return None
  data = str(data)
  remo = 0
  for char in data[::-1]:
    if char == ' ':
      remo -= 1
    else:
      break
  if remo == 0:
    return data
  else:
    return data[:remo]

def len_extracted(data): # Len, discluding leading spaced
  if data == None:
    return 0
  return len(extract(data))

def magnitude(coordA=[0,0], coordB=[0,0]): # Check the magnitude between two coords
    xa = coordA[0]
    ya = coordA[1]
    xb = coordB[0]
    yb = coordB[1]
    return sqrt( (xb-xa)**2 + (yb-ya)**2 )

############### TEXTGRID CLASS ###############

class textGrid:

  
  ########## PROCEDURES ##########

  def __init__(self, defWidth=10, defHeight=10, defSlot=None, emptySlot=' ', cWidth=-1, space=1):
    self.width = int(defWidth)
    self.height = int(defHeight)
    self.slots = self.width * self.height
    self.emptySlot = str(emptySlot)
    self.cellWidth = int(cWidth)
    self.borderSpace = int(space)
    if self.cellWidth < 0:
      if defSlot == None:
        self.cellWidth = len_extracted(str(self.emptySlot))
      else:
        self.cellWidth = len_extracted(str(defSlot))
    self.contents = [[defSlot for row in range(self.height)] for column in range(self.width)]

  def __str__(self): # __str__
    comboList = []
    for X in range(self.width):
      for Y in range(self.height):
        comboList.append(str(self.contents[X][Y]))
        comboList.append(',')
    return comboList

  
  def display(self): # Display the contents of the grid
    for Ycoord in range(self.height):
      for Xcoord in range(self.width):
        item = self.get([Xcoord,Ycoord])
        if item == None:
          print('{0:<{w}}'.format(extract(self.emptySlot), w=self.cellWidth), end='')
        else:
          print('{0:<{w}}'.format(extract(item), w=self.cellWidth), end='')
        print(' '*self.borderSpace, end='')
      print()

  
  def checkCoords(self,coords): # Check if a set of coords is within the grid
    if (-self.height <= coords[1] < self.height) and (-self.width <= coords[0] < self.width):
      return True
    raise IndexError(f'Grid co-ordinates out of range: {coords}')

  
  def refresh(self): # Reformat all grid slots
    for Xcoord in range(self.width):
      for Ycoord in range(self.height):
        self.contents[Xcoord][Ycoord] = self.formatWidth(self.get([Xcoord,Ycoord]))

  
  def reFormat(self): # Check if all grid slots are formatted correctly, and update and refresh if not
    longestLen = len(self.emptySlot)
    for column in self.contents:
      for item in column:
        if len_extracted(item) > longestLen:
          longestLen = len_extracted(item)
    if longestLen != self.cellWidth:
      self.cellWidth = longestLen
  
  def setSlot(self, coords, content=None): # Assign a value to a cell

    Xcoord = coords[0]
    Ycoord = coords[1]
    self.checkCoords(coords)
    self.contents[Xcoord][Ycoord] = extract(content)
    self.reFormat()


  def setPlural(self, coords, content=None): # Assign values to an array of coordinates
    
    singleTypes = (type(None),str,int,float,complex,bool)
    arrayTypes = (list,tuple,range)
    
    if type(coords) not in arrayTypes:
      raise TypeError(f'Expected array type for \'coords\' but received otherwise: {coords}')
    else:
      if type(content) in singleTypes: # singleTypes
        for coord in coords:
          self.setSlot(coord,content)
      elif type(content) in arrayTypes: # arrayTypes
        if len(content) != len(coords):
          raise IndexError(f'Tried to assign array of incorrect length to array of coords: {content}')
        else:
          for n in range(len(coords)):
            self.setSlot(coords[n],content[n])
      else:
        raise TypeError(f'Incompatible data type set to row: {content}, {type(content)} \nAllowed single types: {singleTypes} \nAllowed array types: {arrayTypes}')

    
  def setRow(self, Ycoord, content=None): # Assign value(s) to a row
    
    if Ycoord >= self.height or Ycoord < -self.height:
      raise IndexError(f'Selected assignment row out of range: {Ycoord}')
    self.setPlural(([Xcoord,Ycoord] for Xcoord in range(self.width)),content)

  
  def setColumn(self, Xcoord, content=None): # Assign value(s) to a column

    if Xcoord >= self.width or Xcoord < -self.width:
      raise IndexError(f'Selected assignment row out of range: {Xcoord}')
    self.setPlural(([Xcoord,Ycoord] for Ycoord in range(self.height)),content)

  
  def setSpread(self, content=None, items=1, equalQuantities=True, overlap=False): # Spread out items among a grid

    singleTypes = (type(None),str,int,float,complex,bool)
    arrayTypes = (list,tuple,range)
    
    if items < 1:
      raise IndexError(f'Cannot place less than 1 item in grid: {items}')
    
    coords = []
    if overlap: # overlap == True
      for i in range(items):
        coords.append([rn.randint(0,self.width-1),rn.randint(0,self.height-1)])
    else: # overlap == False
      allCords = [[Xcoord,Ycoord] for Xcoord in range(self.width) for Ycoord in range(self.height)]
      for i in range(items):
        coords.append(allCords.pop(rn.randint(0,len(allCords)-1)))  
    
    if type(content) in singleTypes: # singleTypes
      self.setPlural(coords,content)
    elif type(content) in arrayTypes: # arrayTypes
      contentArray = []
      if equalQuantities == True: ## equalQuantities == True
        for i in range(items):
          contentArray.append(content[i % len(content)])
      elif equalQuantities == False: ## equalQuantities == False
        for i in range(items):
          contentArray.append(rn.choice(content))
      self.setPlural(coords,contentArray)
    else:
      raise TypeError(f'Incompatible data type set to row: {content} \nAllowed single types: {singleTypes} \nAllowed array types: {arrayTypes}')

  
  def setMove(self, coord, destination, duplicate=False): # Moves an item from one slot to another
    content = self.get(coord)
    if duplicate == False:
      self.setSlot(coord)
    self.setSlot(destination, content)


  def setSwap(self, coordA, coordB): # Swap the contents of two locations
    temp_storage = self.get(coordA)
    self.setSlot(coordA, self.get(coordB))
    self.setSlot(coordB, temp_storage)
      
      
  ########## FUNCTIONS ##########

  def get(self, coords): # Retrieve an item from the grid
    return self.contents[coords[0]][coords[1]]
  
  def formatWidth(self, data): # Format a string to a specifc length
    if data == None:
      return None
    try:
      sharpData = extract(str(data))
    except:
      raise TypeError(f'Error formatting data into str: {data}')
    sharpData = '{0:<{w}}'.format(sharpData, w=self.cellWidth)
    return sharpData
    

  def search(self, content=None): # Search for an item in the grid and return a list of coords
    if content != None:
      content = extract(str(content))
    foundCords = []
    for Xcoord in range(self.width):
      for Ycoord in range(self.height):
        if extract(self.get([Xcoord,Ycoord])) == content:
          foundCords.append([Xcoord,Ycoord])
    return foundCords

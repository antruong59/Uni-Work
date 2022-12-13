#
# File: game.py
# Version: 2.0 February 2012
# Description: Problem Solving and Programming
#              Code provided for assignment 2 and practical work.
#

import graphics


class GameBlock():
    def __init__(self, dx, dy, width, height, colour, imageName, blockType, points):
        self.centreX = dx
        self.centreY = dy
        self.width  = width
        self.height = height
        self.colour = colour
        self.imageName = imageName
        self.blockType = blockType
        self.points = points
        self.scrollSpeed = 10
      
        self.block = graphics.Rectangle(graphics.Point(self.centreX-self.width//2, self.centreY-self.height//2),
                                        graphics.Point(self.centreX+self.width//2, self.centreY+self.height//2))
        self.block.setFill(colour)
                
        if not(imageName == None):
          self.image = graphics.Image(graphics.Point(dx,dy), imageName)          
        else:
          self.image = None


    def getBlockType(self):
        return self.blockType


    def setBlockType(self, blockType):
        self.blockType = blockType

        
    def getScrollSpeed(self):
        return self.scrollSpeed


    def setScrollSpeed(self, speed):
        self.scrollSpeed = speed
        

    def getPoints(self):
        return self.points
    
  
    def setPoints(self, points):
        self.points = points


    def getBlock(self):
        return self.block
    

    def getImage(self):
        return self.image


    def getImageName(self):
        return self.imageName

     
    def getColour(self):
        return self.colour
    
  
    def setColour(self, newColour):
        self.colour = newColour
        self.block.setFill(newColour)


    def getCentreX(self):
        return self.centreX


    def getCentreY(self):
        return self.centreY


    def getWidth(self):
        return self.width


    def getHeight(self):
        return self.height


    def move(self, dx, dy):
        self.centreX = self.centreX + dx
        self.centreY = self.centreY + dy

        self.block.move(dx,dy)
        
        if not(self.image == None):
            self.image.move(dx,dy)


    def draw(self, canvas):
        if self.image == None:
            self.block.draw(canvas)
        else:
            self.image.draw(canvas)


    def undraw(self):
        if self.image == None:
            self.block.undraw()
        else:
            self.image.undraw()
        

    


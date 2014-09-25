import sys
#import and init pygame
import pygame
pygame.init() 

# http://www.rapidtables.com/web/color/RGB_Color.htm

#create the screen
window = pygame.display.set_mode((640, 480)) 
pygame.display.set_caption("Titulo")

window.fill((255,255,255))

#draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
pygame.draw.line(window, (0, 0, 0), (0, 0), (30, 50))

#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
        # if event.scancode == 114:
        # print "seta"
        print event.type 
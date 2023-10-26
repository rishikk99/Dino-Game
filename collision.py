import turtle
import pygame

SCREEN_WIDTH = 470
SCREEN_HEIGHT = 320
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
green = (0, 255, 0)
blue = (0, 0, 128)

def crash(x1, y1, x2, y2):
  if (x2 - x1 >= -20) and (x2 - x1 <= 40):
    if (y2 - y1 <= 40):
      return True
  return False

def fixHS(num, name, score):
  #length = len(str(score))
  SPACE = " "
  spaces = 12 - 2 * len(name)
  spaceStr = spaces*SPACE + "          "

  return (str(num) + "." + name + spaceStr + str(score))

def gameOver(score, pressedBack = False):
  global green, blue, SCREEN_WIDTH, SCREEN_HEIGHT, colors

  win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  for i in range(3):
    win.fill((0, 0, 0))
    
    pygame.time.delay(50)
    font = pygame.font.Font('freesansbold.ttf', 52)
    if pressedBack:
      text = font.render('Try Again?', True, green, blue)
    else:
      text = font.render('Game Over!', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 125)
  
    win.blit(text, textRect)
  
    font = pygame.font.Font('freesansbold.ttf', 26)
    text = font.render('Your Score: ' , True, blue, green)
    textRect.center = (SCREEN_WIDTH // 2 + 45, SCREEN_HEIGHT // 2 - 48)

  win.blit(text, textRect)
    
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('Play Again', True, blue, green)
  textRect.center = (SCREEN_WIDTH // 2 + 70, SCREEN_HEIGHT // 2 + 40)

  win.blit(text, textRect)
    
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render('High Scores', True, blue, green)
  textRect.center = (SCREEN_WIDTH // 2 + 60, SCREEN_HEIGHT // 2 + 90)

  win.blit(text, textRect)

  text = font.render(str(score), True, colors[i + 3], colors[i + 4])
  textRect = text.get_rect()
  textRect.center = (SCREEN_WIDTH // 2 + 80, SCREEN_HEIGHT // 2 - 60)
    
  win.blit(text, textRect)
  
  pygame.display.update()
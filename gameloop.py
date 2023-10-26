import pygame
import kinematics, collision
import math, random
import time

scores = []
score = 0
logger = 0.1
scorepairs = {}

pygame.init()
curr = time.time()

SCREEN_WIDTH = 470
SCREEN_HEIGHT = 320

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("DinoGame")

green = (0, 255, 0)
blue = (0, 0, 128)

x = 25
y = 275
width = 40
height = 40
vel = 6
obstaclePos = 0
obstacleSpeed = 5

isJump = False


def resetEverything():
  global run, obstaclePos, isJump, x, y, score, curr, obstacleSpeed, logger
  run = False
  obstaclePos = 0
  isJump = False
  x = 25
  y = 275
  score = 0
  logger = 0.1
  obstacleSpeed = 5
  curr = time.time()


def endScreen():
  run = True
  while run:
    pygame.time.delay(150)

    #Returned to the game over screen
    collision.gameOver(score, True)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if pos[0] > 154 and pos[0] < 323:
          if pos[1] > 174 and pos[1] < 208: # play again
            resetEverything()
            gameloop()
        if pos[0] > 144 and pos[0] < 331: 
          if pos[1] > 224 and pos[1] < 258: # high scores
            highScores()
            run = False

    pygame.display.update()


def highScores():
  color = -1

  global scores
  run = True
  
  while run:
    pygame.time.delay(100)
    win.fill((0, 0, 0))
      
    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render('High Scores', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 125)

    win.blit(text, textRect)

    font = pygame.font.Font('freesansbold.ttf', 32)

    if len(scores) < 6:
      scoresnum = len(scores)
    else:
      scoresnum = 6

    cross = pygame.image.load(r'static/crossmark.png') #Source: https://toppng.com/free-image/red-cross-mark-download-png-red-cross-check-mark-PNG-free-PNG-Images_177748
    
    for i in range(0, scoresnum):
      nextscore = scores[(-1*i)-1]
      text = font.render(collision.fixHS(i+1, scorepairs[nextscore], nextscore), True, blue, green)
      textRect.center = (SCREEN_WIDTH // 2 + 5, SCREEN_HEIGHT // 2 - 30 + (35 * i))
      win.blit(text, textRect)
      win.blit(cross, (40, textRect[1]))

    if scoresnum == 0:
      text = font.render("All scores deleted", True, blue, green)
      textRect.center = (SCREEN_WIDTH // 2 + 5, SCREEN_HEIGHT // 2 - 45)
      win.blit(text, textRect)
      
    color += 1
    if color == 35:
      color = -1

    text = font.render("Back", True, collision.colors[color // 5], (25, 25, 112))
    textRect.center = (150, 25)

    win.blit(text, textRect)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if pos[0] < 75 and pos[1] < 30:
          endScreen()
        elif pos[0] > 40 and pos[0] < 72:
          for i in range(scoresnum):
            bound1 = 103 + 35 * i
            bound2 = 103 + 32 * (i+1)
            if pos[1] > bound1 and pos[1] < bound2:
              scores.pop((-1*i)-1)
              
    pygame.display.update()


def startScreen():
  run = True

  while run:
    win.fill((0, 0, 0))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Welcome to DinoGame', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 75)

    win.blit(text, textRect)
      
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render('Play', True, blue, green)
    textRect.center = (SCREEN_WIDTH // 2 + 110, SCREEN_HEIGHT // 2)

    win.blit(text, textRect)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if pos[0] > 163 and pos[0] < 301:
          if pos[1] > 143 and pos[1] < 210:
            run = False
      pygame.display.update()


def gameloop():
  global curr
  run = True
  curr = time.time()

  dino = pygame.image.load(r'static/rightDino.png') #Source: https://www.dreamstime.com/dinosaur-side-view-d-rendering-isolated-white-background-cute-cartoon-character-image153203298


  while run:
    pygame.time.delay(45)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    keys = pygame.key.get_pressed()
    global x
    if keys[pygame.K_LEFT] and x >= vel:
      x -= vel
      dino = pygame.image.load(r'static/leftDino.png') #Source: https://www.dreamstime.com/dinosaur-side-view-d-rendering-isolated-white-background-cute-cartoon-character-image153203298
      #Image flipped with https://pinetools.com/flip-image
    if keys[pygame.K_RIGHT] and x <= SCREEN_WIDTH - width:
      x += vel
      dino = pygame.image.load(r'static/rightDino.png')

    global isJump
    if not isJump:
      global y
      if keys[pygame.K_SPACE]:
        isJump = True
        jumper = kinematics.Kinematics(y)
    else:
      jumpVal = jumper.continueJump(y)
      if jumpVal == -70:
        isJump = False
        del jumper
      else:
        y = jumpVal

    win.fill((0, 0, 0))

    global obstaclePos, obstacleSpeed, logger
    obstaclePos += obstacleSpeed

    if obstaclePos < 500:
      pygame.draw.rect(win, (0, 255, 0), (480 - obstaclePos, 240, 20, 75))
    else:
      obstaclePos = 0
      logger += 1
      obstacleSpeed += math.log(logger, 10)

    if collision.crash(x, y, 480 - obstaclePos, 240):
      run = False
        
    win.blit(dino, (x, y))

    stopwatch = round((time.time() - curr) * 100)

    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render(str(stopwatch), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (400, 50)

    win.blit(text, textRect)
    
    pygame.display.update()
  
  global score
  score = round((time.time() - curr) * 100)
  scores.append(score)
  scores.sort()

  name = input("Name?\n")
  scorepairs[score] = name[0:6] or name

  run = True

  color = -1
  while run:
    pygame.time.delay(150)

    #loop and conditional, entered screen first time
    collision.gameOver(score, False)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if pos[0] > 154 and pos[0] < 323:
          if pos[1] > 174 and pos[1] < 208: # play again
            resetEverything()
            gameloop()
        if pos[0] > 144 and pos[0] < 331: 
          if pos[1] > 224 and pos[1] < 258: # high scores
            highScores()
            run = False

    pygame.display.update()

  pygame.quit()


class Kinematics:
  #dx = v0t + 1/2 at^2
  a = 0
  v = 0
  starty = 0

  def __init__(self, y, acc = -1.6, vel = 22.4):
    global a
    global v
    global starty
    a = acc
    v = vel
    starty = y

  def continueJump(self, y):
    global starty, v, a
    if starty > y - v:
      v += a
      return y - v
    return -70          # an impossible value


class Geometry:
  # Geometry dash themed - make shapes to dodge

  def __init__(self):
    print("Geometry")
  
  def makeObstacle(self, speed):
    print("Make obstacle")
    

class Platform:
  def __init__(self):
    print("Platform")
  # intitialize platforms to add to level
  # also use isTouching function to determine if touching
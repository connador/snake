from main import pixel, nav


class segment:
  def __init__(self, loc_x, loc_y):
    self.x = loc_x
    self.y = loc_y

class snake:

  def __init__(self, loc_x, loc_y):
    self.x = loc_x
    self.y = loc_y
    self.body = [loc_x, loc_y]
    self.body.append(segment(self.x, self.y))
    self.navigation = nav.n


def move(self):
  length = len(self.body)

  if self.navigation is nav.n:
    self.y += pixel
  elif self.navigation is nav.s:
    self.y += (pixel * -1)
  elif self.navigation is nav.e:
    self.x += pixel
  else:
    self.x += (pixel * -1)

  if length != 1:
    old_tail = self.body[length - 1]






def grow(self):
  self.length += 1
  #self.body.append()

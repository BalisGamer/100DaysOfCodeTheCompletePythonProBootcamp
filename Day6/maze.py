def turn_right():
  turn_left()
  turn_left()
  turn_left()

while not at_goal():
  if right_is_clear() == True:
      if wall_on_right() == False:
          turn_right()
          if front_is_clear() == True:
              move()
      else:
          turn_right()
  else:
      if front_is_clear() == True:
          move()
      elif wall_in_front() == True:
          turn_left()
      else:
          turn_right()
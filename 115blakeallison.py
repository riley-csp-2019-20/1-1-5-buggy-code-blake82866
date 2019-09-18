#   a115_buggy_image.py
import turtle as trtl

# draw the body of the "spider"
drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)

# choose the angle of the legs, the amount, and the position (change pensize also)
legs = 6
leg_length = 70
leg_angle = 360 / legs
drawer.pensize(5)
leg_position = 0

# create the legs
while (n < legs):
  drawer.goto(0,0)
  drawer.setheading(leg_angle*leg_position)
  drawer.forward(leg_length)
  n = n + 1

# hide the turtle from the screen and make the screen freeze
drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()
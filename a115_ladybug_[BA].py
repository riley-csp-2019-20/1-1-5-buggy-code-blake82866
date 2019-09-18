#   a115_ladybutt.py
import turtle as trtl

# identify the ladybutt/drawer
ladybutt = trtl.Turtle()

#create leg length and angles
legs = 6
leg_length = 70
leg_angle = 360/legs
leg_position = 0
ladybutt.pensize(5)

#create legs 
counter = 0
while(counter < legs):
  ladybutt.penup()
  ladybutt.goto(0,-35)
  ladybutt.pendown()
  ladybutt.setheading(leg_angle*leg_position)
  ladybutt.forward(leg_length)
  counter = counter + 1
  leg_position += 1

# create ladybutt head
ladybutt.penup()
ladybutt.setheading(0)
ladybutt.goto(0,0)
ladybutt.pendown()
ladybutt.pensize(40)
ladybutt.circle(5)

# and body
ladybutt.penup()
ladybutt.setheading(0)
ladybutt.goto(0, -55) 
ladybutt.color("red")
ladybutt.pendown()
ladybutt.pensize(40)
ladybutt.circle(20)
ladybutt.setheading(270)
ladybutt.color("black")
ladybutt.penup()
ladybutt.goto(0, 5)
ladybutt.pensize(2)
ladybutt.pendown()
ladybutt.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybutt.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybutt.penup()
  ladybutt.goto(xpos, ypos)
  ladybutt.pendown()
  ladybutt.circle(3)
  ladybutt.penup()
  ladybutt.goto(xpos + 30, ypos + 20)
  ladybutt.pendown()
  ladybutt.circle(2)

  # position next dots
  ypos += 25
  xpos += 5
  num_dots = num_dots + 1

# hide ladybutt and set image as a loop
ladybutt.hideturtle()
wn = trtl.Screen()
wn.mainloop()
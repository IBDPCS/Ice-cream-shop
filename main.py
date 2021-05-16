# Structure chart
# https://gitmind.com/app/doc/59a2304153

import turtle, random

def getRandomColor():
  colors  = ["red","green","blue","orange","purple","pink","yellow"]
  return random.choice(colors)

def draw_ball(t, color, size, x, y):
    t.penup()
    t.color(color)
    t.fillcolor(color)
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    t.circle(size)
    t.penup()
    t.end_fill()
    t.pendown()

def draw_cone(t, size, x, y):
    t.pendown()
    t.color("grey")
    t.fillcolor("grey")
    t.begin_fill()
    t.goto(x,y - 20)
    t.goto(x+10,y)
    t.goto(x-10,y)
    t.goto(x,y - 20)
    t.pendown()
    t.end_fill()
    t.pendown()

def draw_icecream(turtle, color, size, x, y):
    balls = random.choice(range(1,5)) #Choose a random # balls
    print(balls)
    for ball in range(balls):
      yOffset = y + 20 * (ball)
      draw_ball(turtle, color, size, x, yOffset)
    draw_cone(turtle, size, x, y)
    
# https://www.w3schools.com/python/python_for_loops.asp
def draw_row(numIceCreams, rowNum):
  if numIceCreams > 7:
    iceCreams = 7
  else:
    iceCreams = numIceCreams
  
  yOffset = -50+45*rowNum
  
  for num in range(iceCreams):
    xOffset = -170+(rowNum*20)+40*num
    # Note: rowNum*20 offsets so we dont overlap 
    # high ice creams too much
    #print(xOffset)
    color = getRandomColor()  #random.choice(colors) #Choose a random color

    draw_icecream(tommy, color, 10, xOffset, yOffset)


def draw_shop(numRows, numPerRow):
  for num in range(numRows):
    draw_row(numPerRow, num)

#START
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_shop(3, 7)

# tommy.penup()
# tommy.goto(0,-50)
# tommy.color('black')
# tommy.write("Yum!", align="center", font=(None, 16, "bold"))
# tommy.goto(0,-80)
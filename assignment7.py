import turtle
import random
import math

def k():
  t = turtle.Turtle()
  t.rt(90)
  t.fd(100)
  t.rt(180)
  t.fd(50)
  t.rt(45)
  t.fd(75)
  t.rt(180)
  t.fd(75)
  t.rt(270)
  t.fd(75)
  t.clear()
  
def e():
  t = turtle.Turtle()
  t.rt(90)
  t.fd(100)
  t.rt(-90)
  t.fd(50)
  t.rt(180)
  t.fd(50)
  t.rt(90)
  t.fd(50)
  t.rt(90)
  t.fd(50)
  t.rt(180)
  t.fd(50)
  t.rt(90)
  t.fd(50)
  t.rt(90)
  t.fd(50)
  t.clear()

def v():
  t = turtle.Turtle()
  t.rt(75)
  t.fd(100)
  t.rt(-155)
  t.fd(100)
  t.clear()

def i():
  t = turtle.Turtle()
  t.rt(90)
  t.fd(100)
  t.rt(90)
  t.fd(50)
  t.rt(180)
  t.fd(100)
  t.rt(180)
  t.fd(50)
  t.rt(90)
  t.fd(100)
  t.rt(90)
  t.fd(50)
  t.rt(180)
  t.fd(100)
  t.clear()

def n():
  t = turtle.Turtle()
  t.rt(90)
  t.fd(100)
  t.rt(180)
  t.fd(100)
  t.rt(150)
  t.fd(115)
  t.rt(-150)
  t.fd(100)
  t.clear

def p():
  t = turtle.Turtle()
  t.rt(90)
  t.fd(100)
  t.rt(180)
  t.fd(100)
  t.rt(90)

  for i in range (0,180):
    t.fd(0.5)
    t.rt(180/100)

  t.clear()

def f():
  t = turtle.Turtle()
  t.rt(90)
  t.fd(100)
  t.rt(180)
  t.fd(100)
  t.rt(90)
  t.fd(50)
  t.rt(180)
  t.fd(50)
  t.rt(-90)
  t.fd(50)
  t.rt(-90)
  t.fd(50)
  t.clear()

def l():
  t = turtle.Turtle()
  t.rt(90)
  t.fd(100)
  t.rt(-90)
  t.fd(50)
  t.clear()

def kevin():
  k()
  e()
  v()
  i()
  n()

def pfeil():
  p()
  f()
  e()
  i()
  l()

def kelvin():
  k()
  e()
  l()
  v()
  i()
  l()

def flip():
  f()
  l()
  i()
  p()

def smile():
  t = turtle.Turtle()
  t.fd(2)
  t.up()
  t.setposition(50, 0)
  t.down()
  t.fd(2)
  t.up()
  t.setposition(50, -30)
  t.rt(90)
  t.down()
  for i in range (0,180):
    t.fd(0.5)
    t.rt(180/100)
  
  t.clear()

def random_num():
  num = random.randint(1,5)
  return num

def which_word():
  num = random_num()
  if num == 1:
    kevin()
  elif num == 2:
    pfeil()
  elif num == 3:
    kelvin()
  elif num == 4:
    flip()
  elif num == 5:
    smile()
  

def ask_user():
  go_again = True

  while go_again == True:
    num = int(input("How many words would you like generated?"))
    if num < 0:
      print("Invalid number entered! Please try again.")
      go_again = True
    else:
      go_again = False

  for i in range(0, num):
    which_word()

ask_user()
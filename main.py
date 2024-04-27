import turtle
import keyboard

ninja = turtle.Turtle()

while True:
    if keyboard.is_pressed("w"):   
        ninja.forward(10)
    if keyboard.is_pressed("esc"):
       break
    if keyboard.is_pressed("s"):
        ninja.back(10)
    if keyboard.is_pressed("a"):
        ninja.left(5)
    if keyboard.is_pressed("d"):
        ninja.right(5)
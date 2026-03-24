import pgzrun
import random

WIDTH=800
HEIGHT=600
TITLE="mario clicker"
point=0
M=Actor("mario.png")
def draw():
    screen.fill(color="black")
    M.draw()
    screen.draw.text(str(point),(700,100))

def jumpmario():
    M.x=random.randint(0,800)
    M.y=random.randint(0,600)
def on_mouse_down(pos):
    global point
    if M.collidepoint(pos):
        point+=1
        jumpmario()
    else:
        point-=1
        jumpmario()

pgzrun.go()
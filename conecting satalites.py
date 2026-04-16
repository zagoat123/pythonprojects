import pgzrun
from random import randint
WIDTH=535
HEIGHT=300
TITLE="Connecting sattelites"

satellites=[]
number_of_satellite=8
lines=[]
next_satellite=0

def create_satellites():
    for count in range(0, number_of_satellite):
        sat=Actor("satellite")
        sat.pos=randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satellites.append(sat)

def draw():
    screen.blit("space_bg.jpg",(0,0))
    count=1
    for sat in satellites:
        screen.draw.text(str(count),(sat.pos[0],sat.pos[1]+20))
        count += 1
        sat.draw()
    for l in lines:
        screen.draw.line(l[0],l[1],(color="white"))

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite<number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
                next_satellite+=1
        else:
            lines=[]       
            next_satellite=0







create_satellites()
pgzrun.go()
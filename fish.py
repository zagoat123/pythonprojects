import pgzrun
from random import randint
WIDTH=500
HEIGHT=400
TITLE="FINDING FISH"

fish=[]
number_of_fish=5

def create_fish():
    for count in range(0, number_of_fish):
        fis=Actor("fish")
        fis.pos=randint(40, WIDTH-40), randint(40, HEIGHT-40)
        fish.append(fis)
    
def draw():
    screen.blit("water",(0,0))
    for fis in fish:
        fis.draw()


create_fish()
pgzrun.go()
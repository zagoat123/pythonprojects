import pgzrun
import random

WIDTH=600
HEIGHT=500
point=0
flower=Actor("flower.png")
flower.pos=(300,250)
bee=Actor("bee.png")
bee.pos=(150,150)
wasp=Actor("wasp.png")
wasp.pos=(450,350)
def draw():
    screen.blit("background.png",(0,0))
    bee.draw()
    flower.draw()
    wasp.draw()
    screen.draw.text(str(point),color="teal",midtop=(300,50))
def update():
    global point
    if keyboard.down:
        bee.y+=10
    elif keyboard.up:
        bee.y-=10
    elif keyboard.right:
        bee.x+=10
    elif keyboard.left:
         bee.x-=10

    #the code for collecting the flower by za bee
    if bee.colliderect(flower):
        point+=10
        flower.x=random.randint(0,600)
        flower.y=random.randint(0,500)
    if bee.colliderect(wasp):
        point-=5
        wasp.x=random.randint(0,600)
        wasp.y=random.randint(0,500)

pgzrun.go()

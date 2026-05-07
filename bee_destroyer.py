import pgzrun
import random

HIEGHT=500
WIDTH=800
TITLE="BEE DESTROYER"
S=Actor("spaceship")
S.pos=(400,450)
enemies=[]
enemies.append(Actor('bee'))
enemies[-1].x=random.randint(50,750)
enemies[-1].y=-100
bull=[]
score=0
def on_key_down(key):
    if key==keys.SPACE:
        bull.append(Actor('bullet'))
        bull[-1].x=S.x
        bull[-1].y=S.y-50


def draw():
    screen.blit("space_bg",(0,0))
    S.draw()
    for e in enemies:
        e.draw()
    for b in bull:
        b.draw()
    screen.draw.text("score="+str(score),(50,30),color="blue")


def update():
    global score
    if keyboard.left:
        S.x-=10
        if S.x <= 0:
            S.x=0

    if keyboard.right:
        S.x+=10
        if S.x >= WIDTH:
            S.x = WIDTH
    for b in bull:
        b.y-=10
        if b.y<=0:
            bull.remove(b)

    for e in enemies:
        e.y += 5
        if e.y>+HIEGHT:
            e.y=-100
            e.x=random.randint(50,750)
        for b in bull: 
            if e.colliderect(b):
                enemies.remove(e)
                enemies.append(Actor("bee"))
                enemies[-1].x=random.randint(50,WIDTH-50)
                enemies[-1].y=-100
                score+=1







    







pgzrun.go()
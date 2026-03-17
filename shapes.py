import pgzrun
WIDTH=400
HEIGHT=400
TITLE="cool drawing"

def draw():
    #r stores the rectangle
    r=Rect((200,200),(100,110))
    screen.draw.rect(r,color="purple")
    r=Rect((190,200),(90,120))
    screen.draw.rect(r,color="blue")
    r=Rect((180,200),(80,130))
    screen.draw.rect(r,color="red")
    r=Rect((170,200),(70,140))
    screen.draw.rect(r,color="purple")
    r=Rect((160,200),(60,150))
    screen.draw.rect(r,color="red")
    r=Rect((150,200),(50,160))
    screen.draw.rect(r,color="blue")
    r=Rect((140,200),(40,170))
    screen.draw.rect(r,color="red")
    








pgzrun.go()
import pgzrun

WIDTH=500
HEIGHT=490
TITLE="PENALTY"


ball=Actor("football")
ball.pos=(250,375)

post=Actor("post")
post.pos=(250,50)
direction=1
post_speed=3
def draw():
    screen.blit("football_field", (0, 0))
    ball.draw()
    post.draw()


def update():
    global post_speed
    global direction
    if keyboard.space:
        ball.y-=32
    if ball.y<0:
            ball.y=375 
    if keyboard.left:
        ball.x-=10
    if keyboard.right:
        ball.x+=10
    if ball.x<0:
        ball.x=0
    if ball.x>500:
        ball.x=500  

    
    post.x=post_speed*direction
    if post.x>WIDTH-50:  
        direction=-1
    if post.x<50:
        direction=1



pgzrun.go()
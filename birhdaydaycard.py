import pygame
import time 

pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday card!!!")

CYAN=(0, 255, 255)
RED=(255, 0, 0)

font=pygame.font.SysFont("Arial",50)
screen.fill(CYAN)
pygame.display.update()

running=True
shown=False
shown2=False
start_time=time.time()
while running:
    for event in pygame .event.get():
        if event.type==pygame.QUIT:
            running=False

    if not shown and time.time()-start_time>=3:
        screen.fill(CYAN)
        text=font.render("Happy Birthday MOM!",True,RED)
        text_rect=text.get_rect(center=(300,300))

        screen.blit(text,text_rect)
        pygame.display.update()
        shown=True

    if shown and not shown2 and time.time()-start_time>=5:
        screen.fill(CYAN)
        text=font.render("Hope you have the ",True,RED)
        text_rect=text.get_rect(center=(300,250))
        text2=font.render("best birthday ever!!!",True,RED)
        text2_rect=text.get_rect(center=(300,350))

        screen.blit(text,text_rect)
        screen.blit(text2,text2_rect)
        pygame.display.update()
        shown2=True



            
pygame.quit()
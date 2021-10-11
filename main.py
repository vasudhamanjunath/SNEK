import pygame
import time
import random
pygame.init()
width,height=800,600
disp=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNEK")
green,red,black,white=(0,204,153),(255,8,0),(0,0,0),(255,255,255)
font_style=pygame.font.SysFont(None,30)
def gameloop():
    end=0
    x,y,x1,y1=width/2,height/2,0,0
    cell=20
    snake_speed=10
    body,blen=[],1
    clk=pygame.time.Clock()
    food_x=round(random.randrange(0,width-cell)/cell)*cell
    food_y=round(random.randrange(0,height-cell)/cell)*cell
    while not end:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1,y1=-cell,0
                elif event.key==pygame.K_UP:
                    x1,y1=-0,-cell
                elif event.key==pygame.K_RIGHT:
                    x1,y1=cell,0
                elif event.key==pygame.K_DOWN:
                    x1,y1=0,cell
        if x>width or x<0 or y>height or y<0:
            break
        x+=x1;y+=y1
        disp.fill(black)
        pygame.draw.rect(disp,red,[food_x,food_y,cell,cell])
        head=[]
        head.append(x);head.append(y)
        body.append(head)
        for block in body[:blen-1]:
            if block==head:
                end=1
        if len(body)>blen:
            del body[0]
        for block in body:
            pygame.draw.rect(disp,green,[block[0],block[1],cell,cell])
        score=font_style.render("Score: "+str(blen-1),True,white)
        disp.blit(score,[0,0])
        pygame.display.update()
        if food_x==x and food_y==y:
            food_x=round(random.randrange(0,width-cell)/cell)*cell
            food_y=round(random.randrange(0,height-cell)/cell)*cell
            blen+=1
            snake_speed+=0.5;
        clk.tick(snake_speed)
    disp.fill(black)
    m=font_style.render("Game Over",True,red)
    disp.blit(m,[(width/2)-40,height/2])
    f_score=font_style.render("Score: "+str(blen-1),True,white)
    disp.blit(f_score,[(width/2)-25,(height/2)+27])
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
gameloop()
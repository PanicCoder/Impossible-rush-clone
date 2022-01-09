import pygame
import random
pygame.init()
height=350
width=400
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Impossible Rush")
done = False
fps = 60
WHITE=(255,255,255)
i=0
k=0
Colors = [
    (255,0,0),#red
    (255,255,0),#yellow
    (0,255,0),#green
    (0,0,255)#blue
]
class circle():
    def __init__(self):
        pass
    def drop(self,x):
        i=x
        pos = (175,i)
        return pos
class rotate():
    def __init__(self):
        self.first = 0
        self.second = 3
        self.third = 2
        self. forth = 1
    def rotate(self):
        a = self.first
        b= self.second
        c= self.third
        d = self.forth
        self.first = b
        self.second = c
        self.third = d
        self.forth = a
    def get_first(self):
        return self.first
    def get_second(self):
        return self.second
    def get_third(self):
        return self.third
    def get_forth(self):
        return self.forth
class check_colision():
    def __init__(self):
        self.gameover=None
        self.score=0
        self.speed=1
    def win(self):
        if k == rot.get_first() and cir.drop(i) == (175,175) and self.gameover == None :
            self.score +=1
            self.speed += 0.05
        elif  k != rot.get_first() and cir.drop(i)==(175,175):
            self.gameover = True
        else:
            pass
    def get_the_score(self):
        return self.score
    def get_speed(self):
        return self.speed
    def lost(self):
        return self.gameover
cir = circle()
clock = pygame.time.Clock()
rot = rotate()
cos = check_colision()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type ==pygame.MOUSEBUTTONUP:
            rot.rotate()
    i = i+1
    if i > 175:
        i = 0
        k=random.randint(1,3)
    cos.win()
    screen.fill(WHITE)
    if cos.lost():
        lost_font = pygame.font.SysFont('Calibri',25,True,False)
        text_lost = lost_font.render("Game over your Score was "+str(cos.get_the_score()),True,(255,215,0))   
        screen.blit(text_lost, [20,150])
    elif cos.lost() == None:
        pygame.draw.circle(screen,Colors[k],cir.drop(i),20,0)
        pygame.draw.polygon(screen,Colors[rot.get_first()],[[125,150],[225,150],[175,200]],0)
        pygame.draw.polygon(screen,Colors[rot.get_second()],[[125,150],[175,200],[125,250]],0)
        pygame.draw.polygon(screen,Colors[rot.get_third()],[[175,200],[125,250],[225,250]],0)
        pygame.draw.polygon(screen,Colors[rot.get_forth()],[[175,200],[225,150],[225,250]],0)
        score_font = pygame.font.SysFont('Calibri',25,True,False)
        text_score = score_font.render("Score: "+str(cos.get_the_score()),True,(0,0,0))   
        screen.blit(text_score, [0,0])
    clock.tick(fps*cos.get_speed())
    pygame.display.flip()
pygame.quit()
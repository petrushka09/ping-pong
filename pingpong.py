from pygame import *
mixer.init()
mixer.music.load('muzyka.mp3')
mixer.music.play()
font.init()
font=font.Font(None,70)
p1=font.render('Left player wins!',True,(0,0,0))
p2=font.render('Right player wins!',True,(0,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed,lenght,width):
        super().__init__()
        self.image=transform.scale(image.load(img),(lenght,width))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player_r(GameSprite):
    def __init__(self,img,x,y,speed,lenght,width):
        super().__init__(img,x,y,speed,lenght,width)
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>=5 and self.rect.y<=345:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<=345 and self.rect.y>=5:
            self.rect.y+=self.speed
class Player_l(GameSprite):
    def __init__(self,img,x,y,speed,lenght,width):
        super().__init__(img,x,y,speed,lenght,width)
        self.v=self.speed
        self.h=self.speed
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>=5 and self.rect.y<345:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y<=345 and self.rect.y>5:
            self.rect.y+=self.speed
r_racket=Player_r('racket.png',650,200,5,20,150)
l_racket=Player_l('racket.png',30,200,5,20,150)
class Ball(GameSprite):
    def __init__(self,img,x,y,speed,lenght,width):
        super().__init__(img,x,y,speed,lenght,width)
        self.v=self.speed
        self.h=self.speed
    def update(self):
        if self.rect.y>=450 or self.rect.y<=5:
            self.v*=-1
        if sprite.collide_rect(self,r_racket) or sprite.collide_rect(self,l_racket):
            self.h*=-1
        self.rect.x+=self.h
        self.rect.y+=self.v
ball1=Ball('ball.png',300,200,5,50,50)
ball2=Ball('ball.png',300,200,5,30,30)
window=display.set_mode((700,500))
display.set_caption('ping pong')
background=transform.scale(image.load('fon.jpg'),(700,500))
run=True
finish=False
fps=60
clock=time.Clock()
g1=0
g2=0

while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
    if not finish:
        
        clock.tick(fps)
        window.blit(background,(0,0))
        r_racket.reset()
        r_racket.update()
        l_racket.reset()
        l_racket.update()
        ball1.reset()
        ball1.update()
        if ball1.rect.x<=0:
            g2+=1
            ball1.rect.x=300
            ball1.rect.y=200
            if ball1.v>0:
                ball1.v+=1
            if ball1.v<0:
                ball1.v-=1
            if ball1.h>0:
                ball1.h+=1
            if ball1.h<0:
                ball1.h-=1
        if ball1.rect.x>=655:
            g1+=1
            ball1.rect.x=300
            ball1.rect.y=200
            if ball1.v>0:
                ball1.v+=1
            if ball1.v<0:
                ball1.v-=1
            if ball1.h>0:
                ball1.h+=1
            if ball1.h<0:
                ball1.h-=1
        if g1>=5 or g2>=5:
            ball2.reset()
            ball2.update()
            if ball2.rect.x<=0:
                g2+=1
                ball2.rect.x=300
                ball2.rect.y=200
                if ball2.v>0:
                    ball2.v+=1
                if ball2.v<0:
                    ball2.v-=1
                if ball2.h>0:
                    ball2.h+=1
                if ball2.h<0:
                    ball2.h-=1
            if ball2.rect.x>=655:
                g1+=1
                ball2.rect.x=300
                ball2.rect.y=200
                if ball2.v>0:
                    ball2.v+=1
                if ball2.v<0:
                    ball2.v-=1
                if ball2.h>0:
                    ball2.h+=1
                if ball2.h<0:
                    ball2.h-=1
        if g1>=7 or g2>=7:
            if r_racket.speed>0 and l_racket.speed>0:
                r_racket.speed*=-1
                l_racket.speed*=-1

        if g1==10:
            window.blit(p1,(150,200))
            finish=True
        if g2==10:
            window.blit(p2,(150,200))
            finish=True
        t1=font.render('Left player: '+str(g1)+'pts',True,(0,0,0))
        t2=font.render('Right player: '+str(g2)+'pts',True,(0,0,0))
        window.blit(t1,(10,10))
        window.blit(t2,(10,100))
    display.update()

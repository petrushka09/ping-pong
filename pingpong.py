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
        if keys_pressed[K_UP] and self.rect.y>=5:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y<=345:
            self.rect.y+=self.speed
class Player_l(GameSprite):
    def __init__(self,img,x,y,speed,lenght,width):
        super().__init__(img,x,y,speed,lenght,width)
        self.v=self.speed
        self.h=self.speed
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>=5:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect.y<=345:
            self.rect.y+=self.speed
r_racket=Player_r('racket.png',650,200,5,20,150)
l_racket=Player_l('racket.png',30,200,5,20,150)
class Ball(GameSprite):
    def __init__(self,img,x,y,speed,lenght,width):
        super().__init__(img,x,y,speed,lenght,width)
        self.v=self.speed
        self.h=self.speed
    def update(self):
        if self.rect.y==450 or self.rect.y==5:
            self.v*=-1
        if sprite.collide_rect(self,r_racket) or sprite.collide_rect(self,l_racket):
            self.h*=-1
        self.rect.x+=self.h
        self.rect.y+=self.v
ball=Ball('ball.png',300,200,5,50,50)
window=display.set_mode((700,500))
display.set_caption('ping pong')
background=transform.scale(image.load('fon.jpg'),(700,500))
run=True
finish=False
fps=60
clock=time.Clock()

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
        ball.reset()
        ball.update()
        if ball.rect.x==0:
            window.blit(p2,(150,200))
            finish=True
        if ball.rect.x==655:
            window.blit(p1,(150,200))
            finish=True
    display.update()

from pygame import *
from random import *


font.init()
font = font.SysFont('Arial', 36)


# создание окна
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('ping-pong-stol.jpg'), (win_width, win_height))
display.set_caption('ping pong')
clock = time.Clock()
fps = 60




# классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        if keys_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
        

    def update_2(self):
        if keys_pressed[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
            
        if self.rect.y > 500:
            lost += 1
            self.rect.y = 0
            self.rect.x = randint(10, 690)

racket1 = Player('vertical_Line.png', 30, 200, 3, 30, 150)
racket2 = Player('vertical_Line.png', 620, 200, 3, 30, 150)
ball = GameSprite('ball.png', 325, 225, 3, 50, 50)

# переменные
finish = False
game = True
speed_x = 3
speed_y = 3

# игровой цикл
while game == True:
    keys_pressed = key.get_pressed()

    if finish != True:
        window.blit(background, (0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        # отрисовка
        racket1.update_1()
        racket1.reset()
        racket2.update_2()
        racket2.reset()
        ball.reset()
        

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
        
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
    
    if ball.rect.x < 0:
        finish = True
        window.blit(font.render('PLAYER 1 LOSE!', True, (138, 0, 0)), (200, 200))

    if ball.rect.x > win_width:
        finish = True
        window.blit(font.render('PLAYER 2 LOSE!', True, (138, 0, 0)), (200, 200))
            
            
            
     
         

    # получение событий
    for ev in event.get():
        if ev.type == QUIT:
            game = False

        
                    
    
    display.update()
    clock.tick(fps)
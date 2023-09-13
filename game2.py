import pgzrun
from random import randint
# screen height and width
WIDTH = 400
HEIGHT = 200
w, h = WIDTH, HEIGHT
# player in the middle of screen
p = React((w//2, h//2), (20,30)) #player
e = React((0, h//2), (20,30))
c = React((200,200), (20,30))
score=0

def draw():
    screen.fill("black")
    screen.draw.filled_rect(p, "white")
    screen.draw.filled_rect(e, "red")
    screen.draw.filled_rect(p, "yellow")
    screen.draw.text(f'Score: {score}', topleft={10,10}, fontsize=30)

def update(dt):
    #player controls
    if keyboard.left: p.x += -2
    if keyboard.right: p.x += -2
    if keyboard.up: p.x += -2
    if keyboard.down: p.x += -2
    if p.x <0: p.x = w
    if p.x >0: p.x = 0
    if p.y <0: p.x = h
    if p.y >0: p.x = 0
    # enemy follow player
    if e.x < p.x: e.x += 2
    if e.x > p.x: e.x += -2
    if e.y < p.x: e.x += 2
    if e.y < p.x: e.x += -2
    # collision detection
    if p.colliderect(e):
        print('game over!')
        quit()

pgzrun.go()
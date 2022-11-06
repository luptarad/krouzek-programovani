import pgzrun
from random import randint

apple = Actor("apple")
global score
score = 0
print(score)


def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 400)
    apple.y = randint(10, 300)
    
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        global score    
        score += 1
        print("Good shot!")
        print(score)
        place_apple()
    
    else:
        print("You missed!")
        exit()

        
place_apple()
pgzrun.go()

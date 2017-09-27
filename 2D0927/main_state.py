from pico2d import*
import random
import game_framework
import title_state

NowMovingBoy = 10
class Boy:
    global mousePostionX
    global mousePostionY
    global NowMovingBoy

    def __init__(self,num):
        self.x, self.y = random.randint(100, 700), 90
        self.num = num
        self.frame = random.randint(0, 7)
        self.MouseState = False
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.MouseState == True:
            if self.num == NowMovingBoy:
                if mousePostionX < self.x and self.x > 0:
                    self.x -= 5
                elif mousePostionX > self.x and self.x < 800:
                    self.x += 5
                if mousePostionY < self.y and self.y > 0:
                    self.y -= 5
                elif mousePostionY > self.y and self.y < 600:
                    self.y += 5
            self.MouseState = False
        else:
            if self.x < 800:
                self.x += 5
    def updateState(self,state):
        self.MouseState = state
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

def enter():
    global boy, grass, team
    #boy = Boy()
    team = [Boy(i) for i in range(11)]
    grass = Grass()

def exit():
    global boy, grass, team
    del(team)
    del(boy)
    del(grass)

def handle_events():
    events = get_events()
    for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
    global NowMovingBoy
    global running
    global mousePostionX
    global mousePostionY
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_1:
                NowMovingBoy = 1
            elif event.key == SDLK_2:
                NowMovingBoy = 2
            elif event.key == SDLK_3:
                NowMovingBoy = 3
            elif event.key == SDLK_4:
                NowMovingBoy = 4
            elif event.key == SDLK_5:
                NowMovingBoy = 5
            elif event.key == SDLK_6:
                NowMovingBoy = 6
            elif event.key == SDLK_7:
                NowMovingBoy = 7
            elif event.key == SDLK_8:
                NowMovingBoy = 8
            elif event.key == SDLK_9:
                NowMovingBoy = 9
            elif event.key == SDLK_0:
                NowMovingBoy = 0
            elif event.key == SDLK_e:
                NowMovingBoy = 10
        elif event.type == SDL_MOUSEMOTION:
            mousePostionX = event.x
            mousePostionY = 600 - event.y
            for boy in team:
                boy.updateState(True)

def update():
    global boy, team
    for boy in team:
        boy.update()

def draw():
    global boy, team

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    #boy.draw()
    update_canvas()
    delay(0.05)

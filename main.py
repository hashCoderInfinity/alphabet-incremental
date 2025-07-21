# set up lol
import pygame, sys, math
pygame.init()

wn = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Alphebet Grinding Incremental")
clock = pygame.time.Clock()

# var
page_s = "a"
page = 1
clicked = False

# GAME var
point = 0
point_g = 1

# functions
def Text(text, x, y, size, color, font="freesansbold.ttf"):
    ffont = pygame.font.Font(font, size)
    Text_show = ffont.render(text, True,  color)
    wn.blit(Text_show, (x, y))

def Showable(num):
    if num < 10:
        num = math.floor(num * 10) / 10
    else:
        num = math.floor(num)

    return num

class sub_screen_selectors:
    def __init__(self, num, id):
        self.num = num
        self.id = id
    
    def draw(self, color, doit, tcolor, tfont="freesansbold.ttf"):
        x = 0
        y = self.num*100
        self.Rec = pygame.Rect(x, y, 250, 75)
        if doit:    
            pygame.draw.rect(wn, color, self.Rec)

        Text(self.id, x+110, y, 50, tcolor, tfont)

        mouse_pos = pygame.mouse.get_pos()
        if self.Rec.collidepoint(mouse_pos[0], mouse_pos[1]) and clicked:
            global page_s
            page_s = self.id

# loop
FPS = 50
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            mouse_pos = pygame.mouse.get_pos()
            if page_backwardser.collidepoint(mouse_pos[0], mouse_pos[1]):
                page -= 1
            elif page_fronter.collidepoint(mouse_pos[0], mouse_pos[1]):
                page += 1

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    # page setup
    if page == 1:
        sss_a = sub_screen_selectors(0, "a").draw("dark red", True, "red", "C:/Windows/Fonts/agencyr.ttf")

    page_backwardser = pygame.Rect(0, 800, 125, 75)
    pygame.draw.rect(wn, (130, 130, 130), page_backwardser)
    page_fronter = pygame.Rect(125, 800, 125, 75)
    pygame.draw.rect(wn, (160, 160, 160), page_fronter)

    # game
    if page_s == "a":
        # show point
        Text(f"point: {Showable(point)}", 700, 30, 30, "white")
        Text(f"(+{Showable(point_g)}/s)", 750, 60, 10, "white")

    # game functions
    point += point_g / FPS 

    clock.tick(50)
    pygame.display.update()
    wn.fill((0, 0, 0))

    clicked = False
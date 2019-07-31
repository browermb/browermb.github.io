import pygame,random,math
from player import Player
from cell import Cell
from camera import Camera

pygame.init()
colors_players = [(37,7,255),(35,183,253),(48,254,241),(19,79,251),(255,7,230),(255,7,23),(6,254,13)]
colors_cells = [(80,252,54),(36,244,255),(243,31,46),(4,39,243),(254,6,178),(255,211,7),(216,6,254),(145,255,7),(7,255,182),(255,6,86),(147,7,255)]
colors_viruses = [(66,254,71)]
screen_width, screen_height = (800,500)
surface = pygame.display.set_mode((screen_width,screen_height))
t_surface = pygame.Surface((95,25),pygame.SRCALPHA) #transparent rect for score
t_lb_surface = pygame.Surface((155,278),pygame.SRCALPHA) #transparent rect for leaderboard
t_surface.fill((50,50,50,80))
t_lb_surface.fill((50,50,50,80))
pygame.display.set_caption("Agar.io")
cell_list = list()
clock = pygame.time.Clock()
try:
    font = pygame.font.Font("Ubuntu-B.ttf",20)
    big_font = pygame.font.Font("Ubuntu-B.ttf",24)
except:
    print("Font file not found: Ubuntu-B.ttf")
    font = pygame.font.SysFont('Ubuntu',20,True)
    big_font = pygame.font.SysFont('Ubuntu',24,True)

def drawText(message,pos,color=(255,255,255)):
        surface.blit(font.render(message,1,color),pos)

def getDistance(pos1,pos2):
    px,py = pos1
    p2x,p2y = pos2
    diffX = math.fabs(px-p2x)
    diffY = math.fabs(py-p2y)

    return ((diffX**2)+(diffY**2))**(0.5)

#COMPLETE THIS PART
def spawn_cells(numOfCells):
    """add the first line of the for loop
       to run as many times as numOfCells"""
    #The line should go here
        cell = Cell(surface)
        cell_list.append(cell)

def draw_grid():
    for i in range(0,2001,25):
        pygame.draw.line(surface,(230,240,240),(0+camera.x,i*camera.zoom+camera.y),(2001*camera.zoom+camera.x,i*camera.zoom+camera.y),3)
        pygame.draw.line(surface,(230,240,240),(i*camera.zoom+camera.x,0+camera.y),(i*camera.zoom+camera.x,2001*camera.zoom+camera.y),3)

camera = Camera()
blob = Player(surface,"Viliami")
spawn_cells(2000)

def draw_HUD():
    w,h = font.size("Score: "+str(int(blob.mass*2))+" ")
    surface.blit(pygame.transform.scale(t_surface,(w,h)),(8,screen_height-30))
    surface.blit(t_lb_surface,(screen_width-160,15))
    drawText("Score: " + str(int(blob.mass*2)),(10,screen_height-30))
    surface.blit(big_font.render("Leaderboard",0,(255,255,255)),(screen_width-157,20))
    drawText("1. G #1",(screen_width-157,20+25))
    drawText("2. G #2",(screen_width-157,20+25*2))
    drawText("3. ISIS",(screen_width-157,20+25*3))
    drawText("4. ur mom",(screen_width-157,20+25*4))
    drawText("5. w = pro team",(screen_width-157,20+25*5))
    drawText("6. jumbo",(screen_width-157,20+25*6))
    drawText("7. [voz]plz team",(screen_width-157,20+25*7))
    drawText("8. G #3",(screen_width-157,20+25*8))
    drawText("9. doge",(screen_width-157,20+25*9))
    if(blob.mass <= 500):
        drawText("10. G #4",(screen_width-157,20+25*10))
    else:
        drawText("10. Viliami",(screen_width-157,20+25*10),(210,0,0))

while(True):
    clock.tick(70)
    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

            #COMPLETE THIS PART
            """Add if statements for the space key 
                and w key"""
            #the if statement for the space goes here
                blob.split()
            #the if statement for the w goes here
                blob.feed()
        if(e.type == pygame.QUIT):
            pygame.quit()
            quit()

    blob.update()
    camera.zoom = 100/(blob.mass)+0.3
    camera.centre(blob)
    surface.fill((242,251,255))
    draw_grid()
    for c in cell_list:
        c.draw(camera)
    blob.draw(camera)
    draw_HUD()
    pygame.display.flip()
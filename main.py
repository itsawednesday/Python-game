import pygame
import random

fps = 60  # frame rate
main = True
clock = pygame.time.Clock()
# open pygame
pygame.init()
pixel = 40
vel = 2
jump = 0


WIDTH, HEIGHT = 800, 700                            #width800 height600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # create window
cat_SPEED = 0
rat_SPEED = 0
# name of game in screen
pygame.display.set_caption("MouseFishing")


#image
background = pygame.image.load('BG.png')
ratPic = pygame.image.load('rat.png')
catPic = pygame.image.load('animal.png')
picklePic = pygame.image.load('cucumber.png')
lemonPic = pygame.image.load('lemon.png')

# initial location of image
catX = 400
catY = 630
catX_place = 0
ratX = random.randrange(0, WIDTH)
ratY = 100

#multiply
ratPic = []
ratY = []
ratX = []
rat_SPEED = []
more_rats = 5
for i in range(more_rats):
    ratPic.append(pygame.image.load('rat.png'))
    ratX.append(random.randint(0, 750))
    ratY.append(random.randint(50, 120))
    rat_SPEED.append(4)

pickleX = random.randrange(0, WIDTH)
pickleY = 100
pickle_SPEED = 0

picklePic = []
pickleY = []
pickleX = []
pickle_SPEED = []
more_pickle = 3
for i in range(more_pickle):
    picklePic.append(pygame.image.load('cucumber.png'))
    pickleX.append(random.randint(0, 750))
    pickleY.append(random.randint(50, 120))
    pickle_SPEED.append(3)

# score
font = pygame.font.SysFont(None, 25)
scoreValue = 0
textX = 10
textY = 10


def scoreCounter(x, y):
    score = font.render("Score:" + str(scoreValue), True, (0, 0, 0))
    screen.blit(score, (x, y))


# get image on screen
def cat(x, y):
    screen.blit(catPic, (x, y))
def rat(x, y, i):
    screen.blit(ratPic[i], (x, y))
def pickle(x, y, i):
    screen.blit(picklePic[i], (x, y))

def mousecoll():
    global ratY

    # check conditions
    if catY < (ratY[i] + pixel):  # check vertical position

        if ((catX > ratX[i] and catX < (ratX[i] + pixel)) or ((catX + pixel) > ratX[i] and (catX + pixel) < (ratX[i] + pixel))):
            ratY[i] += HEIGHT # if collision happens it will not reappear


def picklecoll():
    global pickleY
    if catY < (pickleY[i] + pixel):
        if ((catX > pickleX[i] and catX < (pickleX[i] + pixel)) or ((catX + pixel) > pickleX[i] and (catX + pixel) < (pickleX[i] + pixel))):
            pickleY[i] += HEIGHT



# while-loop for what is happening inside the loop
while main:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False  #if player exits from game then game stops

            #check direction
        if event.type == pygame.KEYDOWN: # check which key is pressed
            if event.key == pygame.K_LEFT:  # check if key is the left direction
                catX_place = -5  # if left then -5 pixels to left
            if event.key == pygame.K_RIGHT:  # check if key is the right direction
                catX_place = 5  # if right then 5 pixels to right
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   # if keyup arrow is pressed, then coordinates stop changing
                catX_place = 0


            if event.type == pygame.K_SPACE and catY < HEIGHT - pixel:
                jump = 200
            if jump > 0:
                catY -= vel
                jump -= vel
            elif catY < WIDTH - pixel:
                catY += 1




  #  pygame.display.flip()
    clock.tick(fps)


    catX += catX_place # increase value of catX depending on catX_change
# images doesnt go outside the window border
    if catX <= 0:  # image cannot move beyond 0 in x axis
        catX = 0
    elif catX >= 750:  #image stops at 750
        catX = 750

# recalling objects
    for i in range(more_rats):
        ratY[i] = ratY[i] + rat_SPEED[i]
        if ratY[i] > HEIGHT:
            ratY[i] = -10
            ratX[i] = random.randrange(0, (WIDTH - pixel))
        # check for collision with cat

        if mousecoll():
            scoreValue = scoreValue + 1
            ratX[i] = random.randrange(0, 750)
            ratY[i] = random.randrange(50, 200)
        rat(ratX[i], ratY[i], i)

    for i in range(more_pickle):
        pickleY[i] = pickleY[i] + pickle_SPEED[i]
        if pickleY[i] > HEIGHT:
            pickleY[i] = -10
            pickleX[i] = random.randrange(0, (WIDTH - pixel))
        # check for collision with cat
        if picklecoll():
          #  score = score -1
            pickleX[i] = random.randrange(0, 750)
            pickleY[i] = random.randrange(50, 200)
        pickle(pickleX[i], pickleY[i], i)

    cat(catX, catY)
    scoreCounter(textX, textY)

    pygame.display.update()



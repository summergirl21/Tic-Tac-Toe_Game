import random
import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up window
windowSurface = pygame.display.set_mode((375, 375), 0, 32 )
pygame.display.set_caption('Tic-Tac-Toe')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (125, 125, 125)
BLACK = (0, 0, 0)

# set font
basicFont = pygame.font.SysFont(None, 48)

def isPointInSideRect(x, y, rect):
    if x > rect.left and x < rect.right and y > rect.top and y < rect.bottom:
        return True
    else:
        return False

# animation to choose who plays
windowSurface.fill(WHITE)
text1 = basicFont.render('Computer Plays First', True, WHITE, BLACK)
text1Rect = text1.get_rect()
text1Rect.centerx = 188
text1Rect.centery = 125
windowSurface.blit(text1, text1Rect)

text2 = basicFont.render('You Play First', True, WHITE, BLACK)
text2Rect = text2.get_rect()
text2Rect.centerx = 188
text2Rect.centery = 175
windowSurface.blit(text2, text2Rect)

# update the screen
pygame.display.update()

# var to keep track of turns
myTurn = None

while myTurn==None:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if isPointInSideRect(event.pos[0], event.pos[1],text1Rect):
                    myTurn = True
                if isPointInSideRect(event.pos[0], event.pos[1],text2Rect):
                    myTurn = False

windowSurface.fill(WHITE)
# create squares
topLeft = {'rect':pygame.draw.rect(windowSurface, WHITE, (0, 0, 125, 125)), 'is X':False, 'is O':False, 'square':'topLeft', 'type':'corner', 'play':0}
middleLeft = {'rect':pygame.draw.rect(windowSurface, WHITE, (0, 125, 125, 125)), 'is X':False, 'is O':False, 'square':'middleLeft', 'type':'edge', 'play':0}
bottomLeft = {'rect':pygame.draw.rect(windowSurface, WHITE, (0, 250, 125, 125)), 'is X':False, 'is O':False, 'square':'bottomLeft', 'type':'corner', 'play':0}
topMiddle = {'rect':pygame.draw.rect(windowSurface, WHITE, (125, 0, 125, 125)), 'is X':False, 'is O':False, 'square':'topMiddle', 'type':'edge', 'play':0}
middle = {'rect':pygame.draw.rect(windowSurface, WHITE, (125, 125, 125, 125)), 'is X':False, 'is O':False, 'square':'middle', 'type':'middle', 'play':0}
bottomMiddle = {'rect':pygame.draw.rect(windowSurface, WHITE, (125, 250, 125, 125)), 'is X':False, 'is O':False, 'square':'bottomMiddle', 'type':'edge', 'play':0}
topRight = {'rect':pygame.draw.rect(windowSurface, WHITE, (250, 0, 125, 125)), 'is X':False, 'is O':False, 'square':'topRight', 'type':'corner', 'play':0}
middleRight = {'rect':pygame.draw.rect(windowSurface, WHITE, (250, 125, 125, 125)), 'is X':False, 'is O':False, 'square':'middleRight', 'type':'edge', 'play':0}
bottomRight = {'rect':pygame.draw.rect(windowSurface, WHITE, (250, 250, 125, 125)), 'is X':False, 'is O':False, 'square':'bottomRight', 'type':'corner', 'play':0}
squares = [topLeft, middleLeft, bottomLeft, topMiddle, middle, bottomMiddle, topRight, middleRight, bottomRight]
# edges
middleLeft['left'] = topLeft
middleLeft['right'] = bottomLeft
middleLeft['farEdge'] = middleRight
topMiddle['left'] = topRight
topMiddle['right'] = topLeft
topMiddle['farEdge'] = bottomMiddle
bottomMiddle['left'] = bottomLeft
bottomMiddle['right'] = bottomRight
bottomMiddle['farEdge'] = topMiddle
middleRight['left'] = bottomRight
middleRight['right'] = topRight
middleRight['farEdge'] = middleLeft
# corners
topLeft['left'] = topMiddle
topLeft['right'] = middleLeft
topLeft['rightCorner'] = bottomLeft
topLeft['leftCorner'] = topRight
topLeft['farCorner'] = bottomRight
bottomLeft['left'] = middleLeft
bottomLeft['right'] = bottomMiddle
bottomLeft['rightCorner'] = bottomRight
bottomLeft['leftCorner'] = topLeft
bottomLeft['farCorner'] = topRight
topRight['left'] = middleRight
topRight['right'] = topMiddle
topRight['rightCorner'] = topLeft
topRight['leftCorner'] = bottomRight
topRight['farCorner'] = bottomLeft
bottomRight['left'] = bottomMiddle
bottomRight['right'] = middleRight
bottomRight['rightCorner'] = topRight
bottomRight['leftCorner'] = bottomLeft
bottomRight['farCorner'] = topLeft


# draw line on squares
pygame.draw.line(windowSurface, BLACK, (125, 0), (125, 375), 4)
pygame.draw.line(windowSurface, BLACK, (250, 0), (250, 375), 4)
pygame.draw.line(windowSurface, BLACK, (0, 125), (375, 125), 4)
pygame.draw.line(windowSurface, BLACK, (0, 250), (375, 250), 4)

# draw red X
def draw_X(center):
    #print center[0]
    #print center[1]
    x1 = center[0] - 20
    y1 = center[1] - 20
    x2 = center[0] + 20
    y2 = center[1] + 20
    pygame.draw.line(windowSurface, RED, (x1, y1), (x2, y2), 4)
    pygame.draw.line(windowSurface, RED, (x2, y1), (x1, y2), 4)

# draw blue O
def draw_O(center):
    pygame.draw.circle(windowSurface, BLUE, (center[0], center[1]), 25, 4)



# animation if computer wins
def draw_i_won():
    #print "draw i won"
    text = basicFont.render('I Win!', True, BLACK, BLUE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
    windowSurface.blit(text, textRect)

# animation if player wins
def draw_you_won():
    #print "draw you won"
    text = basicFont.render('You Win!', True, BLACK, RED)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
    windowSurface.blit(text, textRect)

# animation if its a tie/cats
def draw_tie():
    text = basicFont.render('Tie :(', True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
    windowSurface.blit(text, textRect)

    # check rows
    if topLeft['is O'] == True and topMiddle['is O'] == True and topRight['is O'] == True:
        return True
    if middleLeft['is O'] == True and middle['is O'] == True and middleRight['is O'] == True:
        return True
    if bottomLeft['is O'] == True and bottomMiddle['is O'] == True and bottomRight['is O'] == True:
        return True

    #check diagonals
    if topLeft['is O'] == True and middle['is O'] == True and bottomRight['is O'] == True:
        return True
    if topRight['is O'] == True and middle['is O'] == True and bottomLeft['is O'] == True:
        return True
    else:
        return False


# combine O_won() and X_won()
def won(player):
    # check Colums
    if topLeft[player] == True and middleLeft[player] == True and bottomLeft[player] == True:
        return True
    if topMiddle[player] == True and middle[player] == True and bottomMiddle[player] == True:
        return True
    if topRight[player] == True and middleRight[player] == True and bottomRight[player] == True:
        return True

    # check rows
    if topLeft[player] == True and topMiddle[player] == True and topRight[player] == True:
        return True
    if middleLeft[player] == True and middle[player] == True and middleRight[player] == True:
        return True
    if bottomLeft[player] == True and bottomMiddle[player] == True and bottomRight[player] == True:
        return True

    #check diagonals
    if topLeft[player] == True and middle[player] == True and bottomRight[player] == True:
        return True
    if topRight[player] == True and middle[player] == True and bottomLeft[player] == True:
        return True
    else:
        return False

def tie():
    squares_played = 0
    for square in squares:
        if square['is X'] == True or square['is O'] == True:
            squares_played = squares_played + 1
    if squares_played == 9:
        return True


# decide which square to play in
def evaluate(squares):
    for square in squares:
        if square['type'] == 'edge':
            if square['left']['is X'] == True or square['right']['is X'] == True:
                square['play'] = square['play'] + 3
            if square['left']['is X'] == True and square['right']['is X'] == True:
                square['play'] = square['play'] + 5
            if middle['is X'] == True and square['farEdge']['is X'] == True:
                square['play'] = square['play'] + 5

            if square['left']['is O'] == True or square['right']['is O'] == True:
                square['play'] = square['play'] + 1
            if square['left']['is O'] == True and square['right']['is O'] == True:
                square['play'] = square['play'] + 5
            if middle['is O'] == True and square['farEdge']['is O'] == True:
                square['play'] = square['play'] + 5

            if square['left']['is O'] == True and square['right']['is X'] == True:
                square['play'] = square['play'] -3
            if square['left']['is X'] == True and square['right']['is O'] == True:
                square['play'] = square['play'] -3

        if square['type'] == 'corner':
            square['play'] = square['play'] + 1
            if square['leftCorner']['is X'] == True or square['rightCorner']['is X'] == True:
                square['play'] = square['play'] + 3
            if square['leftCorner']['is X'] == True and square['rightCorner']['is X'] == True:
                square['play'] = square['play'] + 1
            if square['left']['is X'] == True or square['right']['is X'] == True:
                square['play'] = square['play'] + 1
            if square['left']['is X'] == True and square['right']['is X'] == True:
                square['play'] = square['play'] + 1
            if square['right']['is X'] == True and square['rightCorner']['is X'] == True:
                square['play'] = square['play'] + 3
            if square['left']['is X'] == True and square['leftCorner']['is X'] == True:
                square['play'] = square['play'] + 3
            if middle['is X'] == True and square['farCorner']['is X'] == True:
                square['play'] = square['play'] + 3
            if square['farCorner']['is X'] == True:
                square['play'] = square['play'] + 1

            if square['leftCorner']['is O'] == True or square['rightCorner']['is O'] == True:
                square['play'] = square['play'] + 1
            if square['leftCorner']['is O'] == True and square['rightCorner']['is O'] == True:
                square['play'] = square['play'] + 1
            if square['left']['is O'] == True or square['right']['is O'] == True:
                square['play'] = square['play'] + 1
            if square['right']['is O'] == True and square['rightCorner']['is O'] == True:
                square['play'] = square['play'] + 5
            if square['left']['is O'] == True and square['leftCorner']['is O'] == True:
                square['play'] = square['play'] + 5
            if middle['is O'] == True and square['farCorner']['is O'] == True:
                square['play'] = square['play'] + 5

            if square['left']['is O'] == True and square['leftCorner']['is X'] == True:
                square['play'] = square['play'] - 3
            if square['left']['is X'] == True and square['leftCorner']['is O'] == True:
                square['play'] = square['play'] - 3
            if square['right']['is O'] == True and square['rightCorner']['is X'] == True:
                square['play'] = square['play'] - 3
            if square['right']['is X'] == True and square['rightCorner']['is O'] == True:
                square['play'] = square['play'] - 3

        if square['type'] == 'middle':
            square['play'] = square['play'] + 1
            if topLeft['is X'] == True or topRight['is X'] == True or bottomLeft['is X'] == True or bottomRight['is X'] == True:
                square['play'] = square['play'] + 1
            if middleLeft['is X'] == True or topMiddle['is X'] == True or middleRight['is X'] == True or bottomMiddle['is X'] == True:
                square['play'] = square['play'] + 1
            if topLeft['is X'] == True and bottomRight['is X'] == True:
                square['play'] = square['play'] + 4
            if topRight['is X'] == True and bottomLeft['is X'] == True:
                square['play'] = square['play'] + 4
            if topMiddle['is X'] == True and bottomMiddle['is X'] == True:
                square['play'] = square['play'] + 4
            if middleLeft['is X'] == True and middleRight['is X'] == True:
                square['play'] = square['play'] + 4
            if topLeft['is X'] == True and bottomLeft['is X'] == True:
                square['play'] = square['play'] + 2
            if topRight['is X'] == True and bottomRight['is X'] == True:
                square['play'] = square['play'] + 2


            if topLeft['is O'] == True and bottomRight['is O'] == True:
                square['play'] = square['play'] + 4
            if topRight['is O'] == True and bottomLeft['is O'] == True:
                square['play'] = square['play'] + 4
            if topMiddle['is O'] == True and bottomMiddle['is O'] == True:
                square['play'] = square['play'] + 4
            if middleLeft['is O'] == True and middleRight['is O'] == True:
                square['play'] = square['play'] + 4
        if square['is O'] == True or square['is X'] == True:
            square['play'] = 0

    # print out come of evaluation
    print_play()
    print ' '

    # after find which to play in
    num = 0
    shouldPlay = None
    shouldPlayList = [] # used to randomize play
    for square in squares:
        if square['play'] > num:
            shouldPlay = square
            shouldPlayList = [square]
            num = square['play']
        elif square['play'] == num:
            shouldPlayList.append(square)


        # randomizing play
    if len(shouldPlayList) > 1:
       # print len(shouldPlayList), 'len should play list'
        whichToPlay = random.randrange(0, len(shouldPlayList), 1)
      #  print whichToPlay, 'ran num'
        shouldPlay = shouldPlayList[whichToPlay]
    #for square in shouldPlayList:
     #   print square['square']
     # fix/make better done?

    for square in squares:
        square['play'] = 0
    #print shouldPlay['square'], 'should play'
    return shouldPlay

def print_play():
    print topLeft['play'], topMiddle['play'], topRight['play']
    print middleLeft['play'], middle['play'], middleRight['play']
    print bottomLeft['play'], bottomMiddle['play'], bottomRight['play']



loop = True

# game loop
while loop:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            #if event.button == 1 and myTurn == None:
             #   if isPointInSideRect(event.pos[0], event.pos[1],text1Rect):
              #      myTurn = True
               # if isPointInSideRect(event.pos[0], event.pos[1],text2Rect):
                #    myTurn = False
            if event.button == 1 and myTurn == False:
                for square in squares:
                    rect = square['rect']
                    if isPointInSideRect(event.pos[0], event.pos[1], rect) and square['is X'] == False and square['is O'] == False:
                        draw_X(rect.center)
                        square['is X'] = True
                        myTurn = True

    pygame.display.update()

    if won('is X'):
        #print "You won!!"
        draw_you_won()
        pygame.display.update()
        pygame.time.delay(5000)
        loop = False
        pygame.quit()
        sys.exit

    if won('is O'):
        #print "I won!!"
        draw_i_won()
        pygame.display.update()
        pygame.time.delay(5000)
        loop = False

    if tie():
        #print tie
        draw_tie()
        pygame.display.update()
        pygame.time.delay(5000)
        loop = False

    if myTurn == True:
        willPlay = evaluate(squares)
        draw_O(willPlay['rect'].center)
        willPlay['is O'] = True
        myTurn = False





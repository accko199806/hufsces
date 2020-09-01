import pygame
import pgzrun

INCREASESPEED = 5  # Ball 속도와 패달 속도를 같게 하면 게임이 끝나지 않기 때문에,
PAEELESPEED = 4.5  # 패달 움직이는 속도를 4.5로 줄임 (5 -> 4.5)
TITLE = 'Pong'

WIDTH = 500  # pong-ai는 400x300인데, arena의 크기가 작으면 점수가 나지 않아,
HEIGHT = 400  # 500x400 으로 변경함

WINDOWWIDTH = WIDTH
WINDOWHEIGHT = HEIGHT

# Global Variables to be used through our program
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# width and height of a player paddle
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


# Draws the arena the game will be played in.
def drawArena():
    DISPLAYSURF.fill(BLACK)
    # Draw outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0, 0), (WINDOWWIDTH, WINDOWHEIGHT)), LINETHICKNESS * 2)
    # Draw center line
    pygame.draw.line(DISPLAYSURF, WHITE, (int(WINDOWWIDTH / 2), 0), (int(WINDOWWIDTH / 2), WINDOWHEIGHT),
                     int(LINETHICKNESS / 4))


# Draws the paddle
def drawPaddle(paddle):
    # Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    # Stop paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    # Draws paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)


# draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)


# Ball의 움직임을 수정한 뒤 변경된 값을 리턴함
def moveBall(ball, ballDirX, ballDirY):
    ball.x += (ballDirX * INCREASESPEED)
    ball.y += (ballDirY * INCREASESPEED)
    return ball


# Ball이 엣지에 닿았는지 확인하는 로직
def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == LINETHICKNESS or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY = ballDirY * -1
    if ball.left == LINETHICKNESS or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        ballDirX = ballDirX * -1
    return ballDirX, ballDirY


# Ball이 패달에 닿았는지 확인하는 로직
def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top <= ball.top and paddle1.bottom >= ball.bottom:
        return -1
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top <= ball.top and paddle2.bottom >= ball.bottom:
        return -1
    else:
        return 1


# Checks to see if a point has been scored returns new score
def checkPointScoredLeft(paddle, ball, score, ballDirX):
    # reset points if left wall is hit
    if ball.right == WINDOWWIDTH - LINETHICKNESS:
        score += 1
        return score
    else:
        return score


def checkPointScoredRight(paddle, ball, score, ballDirX):
    if ball.left == LINETHICKNESS:
        score += 1
        return score
    else:
        return score


### ORIGINAL AI (LEFT) ###
def AILeft(ball, ballDirX, paddle):
    # If ball is moving away from paddle, center bat
    if ballDirX == 1:
        if paddle.centery < (WINDOWHEIGHT / 2):
            paddle.y += PAEELESPEED
        elif paddle.centery > (WINDOWHEIGHT / 2):
            paddle.y -= PAEELESPEED
    # if ball moving toward bat, track its movement.
    elif ballDirX == -1:
        if paddle.centery < ball.centery:
            paddle.y += PAEELESPEED
        else:
            paddle.y -= PAEELESPEED
    return paddle


### MAKE NEW AI (RIGHT) ###
def AIRight(ball, ballDirX, ballDirY, paddle):  # Left AI와 반대가 되어야 함
    if ballDirX == -1:  # ballDirX -1 : 왼쪽으로 공이 갈 때, 1 : 오른쪽으로 공이 올 때
        if ball.x <= (WIDTH / 2.5):
            if paddle.centery < (WINDOWHEIGHT / 2):  # 패달이 아래 있는 경우 -> 가운데로 이동시킴
                paddle.y += PAEELESPEED
            elif paddle.centery > (WINDOWHEIGHT / 2):  # 패달이 위에 있는 경우 -> 가운데로 이동시킴
                paddle.y -= PAEELESPEED
    elif ballDirX == 1:  # 공이 오는 경우 2/3선을 기준으로 로직이 바뀌게 설계
        if ball.x >= (WIDTH / 2):  # 공이 2/3선을 넘어온 경우
            if paddle.centery < ball.centery:  # 공이 패달보다 위에 있는 경우
                if ballDirY == -1:  # ballDirY -1 : 올라갈 때, 1 : 내려갈 때 1
                    pass  # 공이 올라가는 경우 천장을 박고 내려오기 때문에 pass 함
                else:  # 공이 내려오는 경우
                    paddle.y += PAEELESPEED  # 공이 천장을 맞고 내려오는 경우이기 때문에, 패달을 위로 올려 공을 맞춤
            else:  # 공이 패달보다 아래 있는 경우
                if ballDirY == 1:  # 공이 내려오는 경우
                    pass  # 바닥을 치고 올라올 것이기 때문에, pass 함
                else:  # 공이 올라오는 경우
                    paddle.y -= PAEELESPEED  # 공이 바닥을 치고 내려오는 경우이기 때문에, 패달을 아래로 내려 공을 맞춤
        else:  # 공이 2/3선을 넘어오지 못한 경우
            if paddle.centery < ball.centery:  # 공이 패달보다 위에 있는 경우
                if ballDirY == -1:  # 공이 올라오는 경우
                    if paddle.centery > 125:  # 공이 천장을 맞고 내려올 확률이 크기 때문에, 패달을 내림
                        paddle.centery -= PAEELESPEED
                else:  # 공이 내려가는 경우
                    if paddle.centery > 125:  # 공이 그대로 내려올 확률이 크기 때문에, 패달을 내림
                        paddle.centery -= PAEELESPEED
            else:  # 공이 패달보다 아래 있는 경우
                if ballDirY == 1:  # 공이 내려가는 경우
                    if paddle.centery < 275:  # 공이 바닥을 치고 올라올 확률이 크기 때문에, 패달을 올림
                        paddle.centery += PAEELESPEED
                else:  # 공이 올라오는 경우
                    if paddle.centery < 275:  # 공이 그대로 올라올 확률이 크기 때문에, 패달을 올림
                        paddle.centery += PAEELESPEED
    return paddle


# Displays the current score on the screen
def displayScore():
    screen.draw.text("LEFT AI : " + str(scoreLeft), (88, 20), color=(255, 255, 255))  # LEFT AI SCORE
    screen.draw.text("RIGHT AI : " + str(scoreRight), (322, 20), color=(255, 255, 255))  # RIGHT AI SCORE


# Initiate variable and set starting positions
# any future changes made within rectangles
ballX = WINDOWWIDTH / 2 - LINETHICKNESS / 2
ballY = WINDOWHEIGHT / 2 - LINETHICKNESS / 2
playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) / 2
playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) / 2
scoreLeft = 0
scoreRight = 0

# Keeps track of ball direction
ballDirX = -1  # -1 = left, 1 = right
ballDirY = -1  # -1 = up, 1 = down

# Creates Rectangles for ball and paddles.
paddle1 = Rect(PADDLEOFFSET, playerOnePosition, LINETHICKNESS, PADDLESIZE)
paddle2 = Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS, PADDLESIZE)
ball = Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

repeat = 0


# pygame.mouse.set_visible(0)  # make cursor invisible
#
# def on_mouse_move(pos):
#     mousex, mousey = pos
#     paddle1.y = mousey

def draw():
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)
    displayScore()


def update():
    global repeat
    global ball
    global ballDirX, ballDirY
    global scoreLeft, scoreRight
    global paddle1, paddle2

    ball = moveBall(ball, ballDirX, ballDirY)
    ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
    scoreLeft = checkPointScoredLeft(paddle1, ball, scoreLeft, ballDirX)
    scoreRight = checkPointScoredRight(paddle2, ball, scoreRight, ballDirX)
    ballDirX = ballDirX * checkHitBall(ball, paddle1, paddle2, ballDirX)
    paddle1 = AILeft(ball, ballDirX, paddle1)
    paddle2 = AIRight(ball, ballDirX, ballDirY, paddle2)  # Custom AI

    if repeat % 60 == 0:  # FPS가 60이므로, 60으로 나누면 1초에 한번씩 출력됨
        print("Repeat Time: ", int(repeat / 60) + 1, " Left: ", scoreLeft, ", Right: ", scoreRight)
    repeat += 1


pgzrun.go()

### 김문업 조교님이 만드신 ai-pong-pgzero 파일 사용 ###
### 기존 오른쪽에 있던 AI를 왼쪽으로 옮기고, 오른쪽 AI를 새로 제작 ###

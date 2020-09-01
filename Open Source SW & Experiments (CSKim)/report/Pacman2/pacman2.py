import pgzrun
import gameinput
import gamemaps
from random import randint
from datetime import datetime

WIDTH = 600
HEIGHT = 660

player = Actor("pacman_o")  # Load in the player Actor image
player.score = 0
player.lives = 3
level = 0
SPEED = 3
GHOSTSPEED = 3  # 고스트의 스피드를 플레이어와 구별함


def draw():  # Pygame Zero draw function
    global pacDots, player
    screen.blit('header', (0, 0))
    screen.blit('colourmap', (0, 80))
    pacDotsLeft = 0
    for a in range(len(pacDots)):
        if pacDots[a].status == 0:
            pacDots[a].draw()
            pacDotsLeft += 1
        if pacDots[a].collidepoint((player.x, player.y)):
            if pacDots[a].status == 0:
                if pacDots[a].type == 2:
                    for g in range(len(ghosts)): ghosts[g].status = 800  # 사탕의 지속시간이 기본 1200이지만, 800으로 줄임
                else:
                    player.score += 10
            pacDots[a].status = 1
    if pacDotsLeft == 0: player.status = 2
    drawGhosts()
    getPlayerImage()
    player.draw()
    drawLives()
    screen.draw.text("LEVEL " + str(level), topleft=(10, 10), owidth=0.5, ocolor=(0, 0, 255), color=(255, 255, 0),
                     fontsize=40)
    screen.draw.text(str(player.score), topright=(590, 20), owidth=0.5, ocolor=(255, 255, 255), color=(0, 64, 255),
                     fontsize=60)
    if player.status == 3: drawCentreText("GAME OVER")
    if player.status == 2: drawCentreText("LEVEL CLEARED!\nPress Enter or Button A\nto Continue")
    if player.status == 1: drawCentreText("CAUGHT!\nPress Enter or Button A\nto Continue")


def drawCentreText(t):
    screen.draw.text(t, center=(300, 434), owidth=0.5, ocolor=(255, 255, 255), color=(255, 64, 0), fontsize=60)


def update():  # Pygame Zero update function
    global player, moveGhostsFlag, ghosts
    if player.status == 0:
        if moveGhostsFlag == 4: moveGhosts()
        for g in range(len(ghosts)):
            if ghosts[g].status > 0: ghosts[g].status -= 1
            if ghosts[g].collidepoint((player.x, player.y)):
                if ghosts[g].status > 0:
                    player.score += 100
                    animate(ghosts[g], pos=(290, 370), duration=1 / SPEED, tween='linear', on_finished=flagMoveGhosts)
                else:
                    player.lives -= 1
                    sounds.pac2.play()
                    if player.lives == 0:
                        player.status = 3
                        music.fadeout(3)
                    else:
                        player.status = 1
        if player.inputActive:
            gameinput.checkInput(player)
            gamemaps.checkMovePoint(player)
            if player.movex or player.movey:
                inputLock()
                sounds.pac1.play()
                animate(player, pos=(player.x + player.movex, player.y + player.movey), duration=1 / SPEED,
                        tween='linear', on_finished=inputUnLock)
    if player.status == 1:
        i = gameinput.checkInput(player)
        if i == 1:
            player.status = 0
            player.x = 290
            player.y = 570
    if player.status == 2:
        i = gameinput.checkInput(player)
        if i == 1:
            init()


def init():
    global player, level
    initDots()
    initGhosts()
    player.x = 290
    player.y = 570
    player.status = 0
    inputUnLock()
    level += 1
    music.play("pm1")
    music.set_volume(0.2)


def drawLives():
    for l in range(player.lives): screen.blit("pacman_o", (10 + (l * 32), 40))


def getPlayerImage():
    global player
    dt = datetime.now()
    a = player.angle
    tc = dt.microsecond % (500000 / SPEED) / (100000 / SPEED)
    if tc > 2.5 and (player.movex != 0 or player.movey != 0):
        if a != 180:
            player.image = "pacman_c"
        else:
            player.image = "pacman_cr"
    else:
        if a != 180:
            player.image = "pacman_o"
        else:
            player.image = "pacman_or"
    player.angle = a


def drawGhosts():
    for g in range(len(ghosts)):
        if ghosts[g].x > player.x:
            if ghosts[g].status > 200 or (ghosts[g].status > 1 and ghosts[g].status % 2 == 0):
                ghosts[g].image = "ghost5"
            else:
                ghosts[g].image = "ghost" + str(g + 1) + "r"
        else:
            if ghosts[g].status > 200 or (ghosts[g].status > 1 and ghosts[g].status % 2 == 0):
                ghosts[g].image = "ghost5"
            else:
                ghosts[g].image = "ghost" + str(g + 1)
        ghosts[g].draw()


def moveGhosts():
    global moveGhostsFlag
    global GHOSTSPEED
    dmoves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # 0 : x + 1
    # 1 : y + 1
    # 2 : x - 1
    # 3 : y - 1
    moveGhostsFlag = 0
    for g in range(len(ghosts)):
        dirs = gamemaps.getPossibleDirection(ghosts[g])
        if inTheCentre(ghosts[g]):  # 초기 init과 플레이어가 잡아 먹었을 때 리스폰 되는 공간
            if ghosts[g].status > 0:  # 플레이어의 SUPER 상태일 때엔 위로 올라가면 잡아먹힐 위험이 있기 때문에 나오지 않음
                pass
            else:
                ghosts[g].dir = 3  # 이외의 경우 밖으로 탈출하여 플레이어를 쫓음
        else:
            if g == 0:  # 플레이어의 위치를 무조건 따라감
                followPlayer(g, dirs)
            if g == 1:  # 플레이어의 위치를 따라가되, 진행 방향을 고수함 (플레이어가 아래로 내려가도 양옆으로 이동하여 이동 경로를 막음)
                followPlayerCurrentPriority(g, dirs)
            if g == 2:  # 플레이어의 위쪽으로 이동함
                followPlayerTop(g, dirs)
            if g == 3:  # 플레이어의 아래쪽으로 이동함
                followPlayerBottom(g, dirs)

        if dirs[ghosts[g].dir] == 0 or randint(0, 50) == 0:
            d = -1
            while d == -1:
                rd = randint(0, 3)
                if aboveCentre(ghosts[g]) and rd == 1:
                    rd = 0
                if dirs[rd] == 1:
                    d = rd
            ghosts[g].dir = d

        if player.score > 3000: GHOSTSPEED = 3.2  # 3천점 이상 넘어갈 시 고스트의 스피드를 높임.
        animate(ghosts[g],
                pos=(ghosts[g].x + dmoves[ghosts[g].dir][0] * 20, ghosts[g].y + dmoves[ghosts[g].dir][1] * 20),
                duration=1 / GHOSTSPEED, tween='linear', on_finished=flagMoveGhosts)


def followPlayer(g, dirs):  # 플레이어를 일방적으로 쫓는 로직
    d = ghosts[g].dir
    if ghosts[g].status > 0:  # 플레이어가 SUPER 상태일 경우
        runFromPlayer(d, player, ghosts, dirs, g)  # 유령이 플레이어에게서 도망감
    else:  # SUPER 상태가 아닌 경우
        if d == 1 or d == 3:
            if player.x > ghosts[g].x and dirs[0] == 1: ghosts[g].dir = 0
            if player.x < ghosts[g].x and dirs[2] == 1: ghosts[g].dir = 2
        if d == 0 or d == 2:
            if player.y > ghosts[g].y and dirs[1] == 1 and not aboveCentre(ghosts[g]): ghosts[g].dir = 1
            if player.y < ghosts[g].y and dirs[3] == 1: ghosts[g].dir = 3


def followPlayerCurrentPriority(g, dirs):  # 현재 상태를 유지하면서 플레이어를 쫓아감.
    d = ghosts[g].dir  # 현재 고스트의 방향
    if ghosts[g].status > 0:  # 플레이어가 SUPER 상태일 경우
        runFromPlayer(d, player, ghosts, dirs, g)  # 유령이 플레이어에게서 도망감
    else:
        if d == 1 or d == 3:  # 1 or 3 : y축 방향인 경우
            if player.y > ghosts[g].y and dirs[1] == 1 and not aboveCentre(
                    ghosts[g]):  # 플레이어가 고스트보다 위에 있는 경우 + 위가 뚫려있을 때
                ghosts[g].dir = 1  # 1 상태 유지
                return
            if player.y < ghosts[g].y and dirs[3] == 1:  # 플레이어가 고스트보다 위에 아래 경우 + 아래가 뚫려있을 때
                ghosts[g].dir = 3  # 3 상태 유지
                return
            if player.x > ghosts[g].x and dirs[0] == 1: ghosts[g].dir = 0  # 플레이어가 고스트 위, 아래에 존재하지만 위아래로 이동이 불가능할 때
            if player.x < ghosts[g].x and dirs[2] == 1: ghosts[g].dir = 2  # 양옆으로 이동한다.
            return
        elif d == 0 or d == 2:  # 0 or 2 : x축 방향인 경우
            if d == 0 and dirs[1] == 0 and aboveCentre(ghosts[g]):  # 왼쪽으로 이동이 가능한 경우
                return
            if player.x > ghosts[g].x and dirs[0] == 1:  # 왼쪽으로 이동해야 하는 경우
                ghosts[g].dir = 0
                return
            if player.x < ghosts[g].x and dirs[2] == 1:  # 오른쪽으로 이동해야 하는 경우
                ghosts[g].dir = 2
                return
            if player.y > ghosts[g].y and dirs[1] == 1 and not aboveCentre(ghosts[g]): ghosts[
                g].dir = 1  # 만약 왼쪽, 오른쪽으로 이동이 불가능할 경우 위로 이동
            if player.y < ghosts[g].y and dirs[3] == 1: ghosts[g].dir = 3  # 만약 플레이어가 고스트의 아래에 있다면 아래로 이동


def followPlayerTop(g, dirs):
    d = ghosts[g].dir  # 현재 고스트의 방향
    if ghosts[g].status > 0:  # 플레이어가 SUPER 상태일 경우
        runFromPlayer(d, player, ghosts, dirs, g)  # 유령이 플레이어에게서 도망감
    else:
        if d == 1 or d == 3:
            if player.x > ghosts[g].x and dirs[0] == 1: ghosts[g].dir = 0
            if player.x < ghosts[g].x and dirs[2] == 1: ghosts[g].dir = 2
        if d == 0 or d == 2:
            if player.y - 50 > ghosts[g].y and dirs[1] == 1 and not aboveCentre(ghosts[g]): ghosts[
                g].dir = 1  # 50을 뺀 값 => 실제 플레이어의 위치보다 상단 위치를 쫓는다.
            if player.y - 50 < ghosts[g].y and dirs[3] == 1: ghosts[g].dir = 3


def followPlayerBottom(g, dirs):
    d = ghosts[g].dir  # 현재 고스트의 방향
    if ghosts[g].status > 0:  # 플레이어가 SUPER 상태일 경우
        runFromPlayer(d, player, ghosts, dirs, g)  # 유령이 플레이어에게서 도망감
    else:
        if d == 1 or d == 3:
            if player.x > ghosts[g].x and dirs[0] == 1: ghosts[g].dir = 0
            if player.x < ghosts[g].x and dirs[2] == 1: ghosts[g].dir = 2
        if d == 0 or d == 2:
            if player.y + 50 > ghosts[g].y and dirs[1] == 1 and not aboveCentre(ghosts[g]): ghosts[
                g].dir = 1  # 50을 다힌 값 => 실제 플레이어의 위치보다 하단 위치를 쫓는다.
            if player.y + 50 < ghosts[g].y and dirs[3] == 1: ghosts[g].dir = 3


def inTheCentre(ga):
    if ga.x > 220 and ga.x < 380 and ga.y > 320 and ga.y < 420:
        return True
    return False


def aboveCentre(ga):
    if ga.x > 220 and ga.x < 380 and ga.y > 300 and ga.y < 320:
        return True
    return False


def flagMoveGhosts():
    global moveGhostsFlag
    moveGhostsFlag += 1


def ghostCollided(ga, gn):
    for g in range(len(ghosts)):
        if ghosts[g].colliderect(ga) and g != gn:
            return True
    return False


def runFromPlayer(d, player, ghosts, dirs, g):  # 유령이 플레이어에게서 도망가는 로직
    if player.movex < 0:  # 플레이어가 왼쪽으로 이동
        if dirs[2] == 1:  # 오른쪽으로 이동이 가능하면 오른쪽으로 이동
            ghosts[g].dir = 2
        elif dirs[1] == 1:  # 위로 이동이 가능하면 위로 이동
            ghosts[g].dir = 1
        elif dirs[3] == 1:  # 아래로 이동이 가능하면 아래로 이동
            ghosts[g].dir = 3
    if player.movex > 0:  # 플레이어가 오른쪽으로 이동
        if dirs[0] == 1:  # 왼쪽으로 이동이 가능하면 왼쪽으로 이동
            ghosts[g].dir = 0
        elif dirs[1] == 1:  # 위로 이동이 가능하면 위로 이동
            ghosts[g].dir = 1
        elif dirs[3] == 1:  # 아래로 이동이 가능하면 아래로 이동
            ghosts[g].dir = 3
    if player.movey > 0:  # 플레이어가 아래로 이동
        if dirs[1] == 1:  # 위로 이동이 가능할 시 위로 이동
            ghosts[g].dir = 1
        elif dirs[0] == 1:  # 왼쪽으로 이동이 가능할 시 왼쪽으로 이동
            ghosts[g].dir = 0
        elif dirs[2] == 1:  # 오른쪽으로 이동이 가능할 시 오른쪽으로 이동
            ghosts[g].dir = 2
    if player.movey < 0:  # 플레이어가 위로 이동
        if dirs[3] == 1:  # 아래로 이동이 가능할 시 아래로 이동
            ghosts[g].dir = 3
        elif dirs[0] == 1:  # 왼쪽으로 이동이 가능할 시 왼쪽으로 이동
            ghosts[g].dir = 0
        elif dirs[2] == 1:  # 오른쪽으로 이동이 가능할 시 오른쪽으로 이동
            ghosts[g].dir = 2


def initDots():
    global pacDots
    pacDots = []
    a = x = 0
    while x < 30:
        y = 0
        while y < 29:
            d = gamemaps.checkDotPoint(10 + x * 20, 10 + y * 20)
            if d == 1:
                pacDots.append(Actor("dot", (10 + x * 20, 90 + y * 20)))
                pacDots[a].status = 0
                pacDots[a].type = 1
                a += 1
            if d == 2:
                pacDots.append(Actor("power", (10 + x * 20, 90 + y * 20)))
                pacDots[a].status = 0
                pacDots[a].type = 2
                a += 1
            y += 1
        x += 1


def initGhosts():
    global ghosts, moveGhostsFlag
    moveGhostsFlag = 4
    ghosts = []
    g = 0
    while g < 4:
        ghosts.append(Actor("ghost" + str(g + 1), (270 + (g * 20), 370)))
        ghosts[g].dir = 1
        ghosts[g].status = 0
        g += 1


def inputLock():
    global player
    player.inputActive = False


def inputUnLock():
    global player
    player.movex = player.movey = 0
    player.inputActive = True


init()
pgzrun.go()

# 추격 방법
# 1. 플레이어의 위치를 무조건 쫓아가는 고스트 1
# 2. 플레이어를 쫓아가되, 플레이어의 가는 방향을 막는 고스트 2
# 3. 플레이어의 상단을 쫓아가 탈출구를 막는 고스트 3
# 4. 플레이어의 하단을 쫓아가 탈출구를 막는 고스트 4
# 5. 플레이어의 점수가 3천점이 넘을 시 고스트의 이동 속도를 3.2로 변경
# 6. 사탕의 기본 지속 시간이 1200인데, 800으로 줄여 사용자가 고스트를 위협하는 시간을 줄임

# 플레이어가 사탕을 먹으면 도망가는 로직
# 1. 플레이어가 위로 이동 시 아래로 이동, 아래로 이동 시 위로 이동
# 2. 플레이어가 왼쪽으로 이동 시 오른쪽으로 이동, 오른쪽으로 이동 시 왼쪽으로 이동
# 3. 만약 위 아래, 혹은 양 옆이 막혀있다면 차선택으로 양옆, 위 아래로 이동시켜 탈출로를 생성

# 수정된 파일
# pacman2.py 만 수정됨

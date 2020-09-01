import pgzrun

WIDTH = 700
HEIGHT = 650
TITLE = 'Connect 4'

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW = 6
COLUMN = 7

stage = 0
circle = 100
colRegion = [0, 0, 0, 0, 0, 0, 0]
game_over = False
winner = ""

tileStatus = [  # column = 7, row = 6, 2차원 배열 생성
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]


class Tile:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def contains(self, px, py):
        return self.x < px < self.x + self.width and self.y < py < self.y + self.height


def findMousePointCol(px, py):
    for i in range(0, len(colRegion)):
        if colRegion[i].contains(px, py):
            return i
    return -1


def checkWinner(ro, co):  # 이긴 사람을 체크하는 로직
    winner = tileStatus[ro][co]

    # case N-S
    lcount = 0
    rcount = 0
    k = 1
    while ro + k < ROW:
        if winner == tileStatus[ro + k][co]:
            lcount += 1
        else:
            break
        k += 1
    if lcount + rcount + 1 >= 4:
        return winner

    # case W - E
    winner = tileStatus[ro][co]
    lcount = 0;
    k = 1
    while co - k >= 0:
        if winner == tileStatus[ro][co - k]:
            lcount += 1
        else:
            break
        k += 1

    rcount = 0
    k = 1
    while co + k < COLUMN:
        if winner == tileStatus[ro][co + k]:
            rcount += 1
        else:
            break
        k += 1

    if lcount + rcount + 1 >= 4:
        return winner

    # case NE - SW
    winner = tileStatus[ro][co]
    lcount = 0
    k = 1
    while co - k >= 0 and ro + k < ROW:
        if winner == tileStatus[ro + k][co - k]:
            lcount += 1
        else:
            break
        k += 1

    rcount = 0
    k = 1
    while co + k < COLUMN and ro - k >= 0:
        if winner == tileStatus[ro - k][co + k]:
            rcount += 1
        else:
            break
        k += 1
    if lcount + rcount + 1 >= 4:
        return winner

    # case NW - SE
    winner = tileStatus[ro][co]
    lcount = 0
    k = 1
    while co - k >= 0 and ro - k >= 0:
        if winner == tileStatus[ro - k][co - k]:
            lcount += 1
        else:
            break
        k += 1
    rcount = 0
    k = 1
    while co + k < COLUMN and ro + k < ROW:
        if winner == tileStatus[ro + k][co + k]:
            rcount += 1
        else:
            break
        k += 1
    if lcount + rcount + 1 >= 4:
        return winner

    return 0  # no winner


def draw():
    screen.fill(BLUE)  # 배경을 파란색으로 설정함

    for c in range(COLUMN):  # column = 7
        for r in range(ROW):  # row = 6
            if tileStatus[r][c] == 0:  # 아무도 선택하지 않았을 때
                # position, round, width, color
                screen.draw.filled_circle((int(c * circle + circle / 2), int(r * circle + circle / 2)), 40, WHITE)
            elif tileStatus[r][c] == 1:  # 빨간팀이 선택했을 때
                screen.draw.filled_circle((int(c * circle + circle / 2), int(r * circle + circle / 2)), 40, RED)
            elif tileStatus[r][c] == 2:  # 노란팀이 선택했을 때
                screen.draw.filled_circle((int(c * circle + circle / 2), int(r * circle + circle / 2)), 40, YELLOW)

    for c in range(COLUMN):  # column = 7
        colRegion[c] = Tile((c * circle), 0, circle, HEIGHT - 50)  # 눌렀을 때 위치를 반환할 Tile 추가

    screen.draw.filled_rect(Rect((0, 605), (700, 95)), WHITE)  # 게임 결과를 출력할 부분

    if game_over:  # 게임오버가 되면 결과 출력
        screen.draw.text("Winner is " + str(winner), (15, 620), color=(0, 0, 0))  # 승자 표시
        screen.draw.text("Retry", (645, 620), color=(0, 0, 0))  # Retry 버튼


def update():
    pass


def on_mouse_down(pos):  # Click Event
    global stage
    global game_over
    global winner
    global tileStatus

    col = findMousePointCol(pos[0], pos[1])
    bot = 0
    if not game_over and col != -1:  # 게임이 끝나지 않았을 경우 and 누른 위치가 -1이 아닐 경우
        if tileStatus[0][col] == 0:  # 모두 채워졌는지 확인. 이 조건문이 없으면 맨 위의 값이 계속 바뀌게 됨.
            for i in range(ROW - 1, -1, -1):  # 5부터 0까지 -1 단위로 줄어들게 함.
                if tileStatus[i][col] == 0:
                    bot = i
                    break
            print(col, bot)

            if stage % 2 == 0:
                tileStatus[bot][col] = 2
            else:
                tileStatus[bot][col] = 1
            stage += 1

            winner = checkWinner(bot, col)
            if winner != 0:
                mark = ["", "Red", "Yellow"]
                print(mark[winner])
                game_over = True
                winner = mark[winner]

    if 645 <= pos[0] <= 685 and 620 <= pos[1] <= 635:  # Retry 버튼을 눌렀을 때 이벤트
        tileStatus = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        game_over = False
        stage = 0


pgzrun.go()

# 터틀런 만들기
import turtle as t
import random
import time

score = 0           # 점수를 저장하는 변수
playing = False     # 현재 게임 플레이 중인지 확인하는 변수
tspeed = 3

iqRange = 20

win = t.Screen()
win.register_shape('tenor.gif')

te = t.Turtle()     # 악당 거북이(빨간색)
te.shape('tenor.gif')
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()     # 먹이(초록색 동그라미)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

ta = t.Turtle()
ta.shape("triangle")
ta.color("blue")
ta.speed(0)
ta.up()
ta.goto(0, 50)

writer = t.Turtle()
writer.color("red")
writer.up()
writer.goto(200, 200)
writer.hideturtle()

def turn_right():                # 오른쪽으로 방향을 바꿉니다.
    t.setheading(0)

def turn_up():                   # 위로 방향을 바꿉니다.
    t.setheading(90)

def turn_left():                 # 왼쪽으로 방향을 바꿉니다.
    t.setheading(180)

def turn_down():                 # 아래로 방향을 바꿉니다.
    t.setheading(270)

def push_A():
    global score
    for i in range(40):
        t.forward(2)
    
def start():                    # 게임을 시작하는 함수
    global playing
    if playing == False:
        playing = True
        t.clear()               # 메시지를 지웁니다
        play()

def play():                     # 게임을 실제로 플레이하는 함수
    global score
    global playing
    global tspeed
    for i in range(tspeed):
        t.forward(5)

    writer.clear()
    writer.write("score: " + str(score))

    if score == 5: iqRange = 15
    elif score == 10: iqRange = 10
    elif score == 15: iqRange = 5
    if random.randint(1, 20) == 3:       # 1~5 사이에서 뽑은 수가 3이면(20% 확률)
        ang = te.towards(t.pos())
        te.setheading(ang)              # 악당 거북이가 주인공 거북이를 바라보게 합니다.
    speed = score + 2           # 점수에 5를 더해서 속도를 올립니다(점수가 올라가면 빨라집니다).
    for x in range(speed):
        if random.randint(1, 50) == 3:       # 1~5 사이에서 뽑은 수가 3이면(20% 확률)
            ang = te.towards(t.pos())
            te.setheading(ang)              # 악당 거북이가 주인공 거북이를 바라보게 합니다.
        te.forward(5)
        
    if t.distance(te) < 30:             # 주인공과 악당의 거리가 12보다 작으면 게임을 종료합니다.
        text = "Score : " + str(score)
        message("Game Over", text, "you bad")
        playing = False
        score = 0

    if t.distance(ts) < 30:             # 주인공과 먹이의 거리가 12보다 작으면(가깝게 있으면)
        score = score + 1               # 점수를 올립니다.
        star_x = random.randint(-250, 250)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)         # 먹이를 다른 곳으로 옮깁니다.

    if t.distance(ta) < 30:             # 주인공과 레벨의 거리가 12보다 작으면(가깝게 있으면)
        tspeed = tspeed + 2
        t.write("turtle spped : " + str(tspeed))                  # 스피드를 화면에 표시합니다.
        star2_x = random.randint(-250, 250)
        star2_y = random.randint(-230, 230)
        ta.goto(star2_x, star2_y)         # 레벨을 다른 곳으로 옮깁니다.

    x = t.position()[0]
    y = t.position()[1]
    if not -250 < x < 250:
        ang = 360 - te.towards(t.pos())
        t.setheading(ang)

    if playing:
        t.ontimer(play, 200)            # 게임 플레이 중이면 0.1초 후 play 함수를 실행합니다.

def message(m1, m2, m3):                    # 메시지를 화면에 표시하는 함수
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 30))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 25))
    t.goto(0, -135)
    t.write(m3, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")   # 거북이 모양의 커서를 사용합니다.
t.speed(0)          # 거북이 속도를 가장 빠르게로 지정합니다
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")   # [→]를 누르면 turn_right 함수를 실행하도록 합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(push_A, "a")
t.onkeypress(start, "space")
t.listen()          # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
message("Turtle Run", "[Space]", "Make By virepus")

#   [출처] 파이썬 터틀런 게임(python turtle run game) [2021 04 10 ~ 23]|작성자 MIN



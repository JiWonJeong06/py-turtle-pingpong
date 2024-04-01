import turtle as t
import random
import time
def R():
    if player.xcor() < 200:
        player.forward(10)
def L():
    if player.xcor() > -200:
        player.backward(10)


t.bgcolor('skyblue')
t.setup(500.700)



#플레이어
player = t.Turtle()
player.shape('square')
player.color('pink')
player.shapesize(1, 5)
player.up()
player.speed(0)
player.goto(0, -270)

#공
ball = t.Turtle()
ball.shape('circle')
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color('white')



t.listen()
t.onkeypress(R, 'Right')
t.onkeypress(L, 'Left')

ball_xspeed = 5
ball_yspeed = 5

#게임시작
game_on = True
heart = 3
t.up()
t.ht()
t.goto(0,300)
t.write(f'하트 : {heart} ', False, 'center',("",20))
score = 0
match = t.Turtle()
match.up()
match.ht()
match.goto(0,-320)
match.write(f'점수 : {score} 점', False, 'center',("",20))
while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1
    
    if ball.ycor() > 340:
        ball_yspeed *= -1

    if ball.ycor() < -340:
        heart -= 1
        t.clear()
        t.write(f'하트 : {heart}', False, 'center',("",20))
        time.sleep(0.5)
        ball.goto(0, 100)
        ball_yspeed *= -1
        ball_xspeed *= -1

    if heart == 0:
        game_on = False
        t.goto(0, 0)
        t.write('게임종료', False, 'center',("",20))
        

    if player.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1
        score += 1
        match.clear()
        match.write(f'점수 : {score} 점', False, 'center',("",20))
         
        
    





t.done()
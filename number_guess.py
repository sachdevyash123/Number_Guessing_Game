import random
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
Number=0
chances=7
x=""
win=False
 
def draw_handler(canvas): # Draw Handler Function
# global n
 global x
 frame.set_canvas_background("white")
 canvas.draw_text("Chances Left:",(30,30),40,'red')
 canvas.draw_text(str(chances),(250,30),40,'red')
 canvas.draw_text(x,(60,60),20,'red')
 
def guess(num):
 global chances,Number,x,win
 if win==False:
    if chances!=0:
        if(int(num)>Number):
            x="Number is Lower"
        elif(int(num)<Number):
            x="Number is Higher"
        else:
            x="You Win"
            win=True
        chances=chances-1
    if(chances==0):
        x="You Lose,The Number was "+str(Number)
def range100():
 global chances,Number,x
 Number=random.randint(1,100)
 x=" "
 chances=7
def range1000():
 global chances,Number,x
 Number=random.randint(1,1000)
 chances=12
 x=" "
frame=simplegui.create_frame("Testing",400,400) 
inp1=frame.add_input("Guess the No",guess,50) #input function
button1=frame.add_button("Range 0-100",range100,100)
button2=frame.add_button("Range 0-1000",range1000,100)
frame.set_draw_handler(draw_handler)
#Start
frame.start()
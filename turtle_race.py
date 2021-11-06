# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:16:00 2021

@author:  nilay """


from turtle import Turtle , Screen 
import random 


#Screen 
screen = Screen()
screen.setup(width = 500 , height = 400)
screen.title("Turtle Betting!") 



colors = ['Red', 'Orange' , 'Yellow' , 'Green', 'Blue', 'Indigo' ,  'Violet' ]
turtles = list() 
posny = -150 
check = False  
 


def position(val) : 
    global posny
    turtles[val].shape('turtle')
    turtles[val].penup()
    turtles[val].goto(-230,posny)
    turtles[val].fillcolor(colors[val])
    posny = posny + 50
    


def movement() : 
        posnx = 0
        global check  
        while check == True : 
            win = 0 
            for turtle in turtles : 
                distance = random.randint(0,10) 
                turtle.fd(distance)
                posnx = posnx + distance 
                win = win + 1 
                if turtle.xcor() >= 230 :                  
                    check = False 
                    return(win) 
              
            
#creating multiple turtles 
turtles =  [Turtle() for i in range(7)] 



 
user_bet = screen.textinput( title = 'Make your Bet ', prompt = 'Which turtle will win the race ? enter the color' ).title()
print(user_bet)



 
for i in range(7) : 
    position(i) 


for i in range(7) :
    if user_bet == colors[i] :
        winner_bet = i 
 

if user_bet : 
    check = True 
    
    
winner = movement()  



if colors[winner_bet] == colors[winner-1] : 
    print('You win!') 
    print(colors[winner-1 ]) 
else : 
    print('You lost!') 
    print(colors[winner-1 ]) 
    


 
screen.listen()

screen.exitonclick()

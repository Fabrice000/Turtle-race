from turtle import Turtle, Screen
from random import randint
from tkinter import messagebox
colors = ["red", "green", "blue", "orange", "purple", "yellow"]
turtle_list = []
    
screen = Screen()
screen.setup(height=400, width=500 )

def create_turtle(x = -230,y = -100):
    for color in colors: 
        new_turtle = Turtle("turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=x,y=y)
        turtle_list.append(new_turtle)
        y += 50

def race():
    is_ok = False
    while not is_ok:
        user_input = screen.textinput(title="make your bed", prompt="Which turtle will win the race (red/blue/green/orange/purple/yellow) .Enter your choice:")
        if user_input.lower() in colors:
            is_ok = True
        elif user_input.lower() == "exit":
            if messagebox.askyesno(title="Exit",message="Do you want to exit?"):
                screen.bye()
        else:
            messagebox.showerror(title="Colors", message="Please enter an existant color")
    is_race_on = False

    
    if user_input:
        is_race_on = True
    create_turtle()
    while is_race_on:
        
        for turtle in turtle_list:
            if turtle.xcor() > 225:
                is_race_on = False
                winning_color = turtle.pencolor()
                if user_input == winning_color:
                    print(f"You win the {user_input} turtle win the race!")
                else:
                    print(f"You lose. The {winning_color} turtle win the race!")
                
            random_distance = randint(0,10)
            turtle.forward(random_distance)
    replay()
        
def replay():
    
    if messagebox.askquestion(title="Replay",message="Do you want to retry?"):
        for turtle in turtle_list:
            turtle.hideturtle()
            turtle.goto(-1000,1000)
        race()
    else:
        return 0
        
race()

    

screen.exitonclick()

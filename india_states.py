from turtle import Screen, Turtle
import pandas as pd

# here we create 2 turtle objects 1. 'turtle', 2. 't.' because 1st object is used to display map
# and other object is used to display state names.

turtle = Turtle()
screen = Screen()

# global score variable
SCORE = 0

image = "map.gif"

# this enables the shape of turtle to image we provide
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("india_states_coordinates.csv")
all_states = data["state"].to_list()     # convert states column of csv to a list
correct_guesses = []                     # empty list to store correct guesses of user

while len(correct_guesses) < 50:         # length is set to less than 50 because total 50 states are there in csv

    screen.title(f"U.S states game")

    # this variable stores the guess of the user and converts it to title case using .title() function
    state_guess = screen.textinput(title=f"{SCORE}/50 States Correct!", prompt="Enter state name here").title()

    # MAIN LOGIC for quiting game and creating csv file for non-guessed states

    if state_guess == "Exit":                  # 'Exit' ends the game and closes the window

        missing_states = [state for state in all_states if state not in correct_guesses]    # list comprehension

        # this loop checks the states not in correct_guess and appends it to missing_state
        # for state in all_states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)

        # a new_file variable is created to make a dataFrame of missing_states
        new_file = pd.DataFrame(missing_states)

        # this file is converted to a csv
        new_file.to_csv("states_to_learn.csv")

        # exits the main while loop
        break

    # MAIN LOGIC for correct guess and keeping score

    if state_guess in all_states:
        correct_guesses.append(state_guess)
        SCORE += 1
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state_guess]  # extracts the tuple whose state is equal to guessed state
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_guess)            # can also use 'state_data.state.item()' as argument in write()

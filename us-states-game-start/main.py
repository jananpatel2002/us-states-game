import pandas
import turtle

screen = turtle.Screen()
screen.title("US STATES GAME")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data['state'].to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States are Correct.",
                                    prompt="What's another state's name? ").title()
    if answer_state == 'Exit':
        break
    for state in states_list:
        if state == answer_state:
            correct_guesses.append(state)
            state_info = states_data[states_data['state'] == state]  # Filters out only state that == the answer
            x = int(state_info.x)
            y = int(state_info.y)
            text = turtle.Turtle()
            text.shape('circle')
            text.shapesize(.1,.1)
            text.penup()
            text.goto(x, y)
            text.write(answer_state)

missing_states_list = []
for state in states_list:
    if state not in correct_guesses:
        missing_states_list.append(state)

sd = pandas.DataFrame(missing_states_list)
sd.to_csv('states_to_learn.csv')
screen.exitonclick()

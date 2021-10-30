import turtle
import pandas
FONT = ("Courier", 6, "normal")
screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
data = pandas.read_csv("50_states.csv")

state_counter = 0

all_states = data.state.tolist()
print(all_states)

correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"Guess the State {state_counter}/50", prompt="Whats another state's name")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        need_help = [state for state in all_states if state not in correct_answers]
        # states_to_learn.csv

        df = pandas.DataFrame(need_help)
        df.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:

        state_name_turtle = turtle.Turtle()
        state_name_turtle.hideturtle()
        state_name_turtle.penup()
        state_name_turtle.color('Black')
        state_x = data.x[data.state == answer_state]
        state_y = data.y[data.state == answer_state]
        state_name_turtle.goto(int(state_x),int(state_y))
        state_name_turtle.write(f"{answer_state}", False, "center", FONT)

        state_counter += 1
        correct_answers.append(answer_state)










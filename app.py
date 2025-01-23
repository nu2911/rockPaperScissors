from flask import Flask, render_template, request
import random

app = Flask(__name__)

# user choice in arg (will come from frontend)
userWins = 0
computerWins = 0
draw = 0
def playGame(userChoice):
    global userWins, computerWins, draw
    choices = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(choices)

    # r>s p>r s>p  gameLogic
    if userChoice == computerChoice:
        result = "It's a tie!"
        draw = draw+1
    elif (userChoice == 'rock' and computerChoice == 'scissors') or (userChoice == 'paper' and computerChoice == 'rock') or ( userChoice == 'scissors' and computerChoice == 'paper'):
        result = "You win!"
        userWins = userWins+1
    else:
        result = "You lose!"
        computerWins = computerWins+1

    return result, computerChoice

@app.route('/')
def index():
    global userWins, computerWins, draw
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    userChoice = request.form.get('userChoice')  
    if userChoice is None:
        return "Error: No choice selected", 400  
    result, computerChoice = playGame(userChoice)
    return render_template('index.html', userChoice=userChoice, computerChoice=computerChoice, result=result, draw=draw, userWins=userWins, computerWins=computerWins)

@app.route('/reset')
def reset():
    global userWins, computerWins, draw
    userWins, computerWins, draw = 0, 0, 0  
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
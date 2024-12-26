from flask import Flask, render_template, request
import random

app = Flask(__name__)

# user choice in arg (will come from frontend)
def playGame(userChoice):
    choices = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(choices)

    # r>s p>r s>p  gameLogic
    if userChoice == computerChoice:
        result = "It's a tie!"
    elif (userChoice == 'rock' and computerChoice == 'scissors') or (userChoice == 'paper' and computerChoice == 'rock') or ( userChoice == 'scissors' and computerChoice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    return result, computerChoice


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/play', methods=['POST'])
# def play():
#     userChoice = request.form.get('userChoice')
#     computerChoice, result = playGame(userChoice)

#     return render_template(index.html, userChoice=userChoice, computerChoice=computerChoice, result=result)

@app.route('/play', methods=['POST'])
def play():
    # Get the user's choice from the form
    userChoice = request.form.get('userChoice')  # Correct way to get form data
    
    if userChoice is None:
        return "Error: No choice selected", 400  # Handle case where no choice is made
    
    # Get the result from the game logic
    result, computerChoice = playGame(userChoice)

    return render_template('index.html', userChoice=userChoice, computerChoice=computerChoice, result=result)


if __name__ == '__main__':
    app.run(debug=True)

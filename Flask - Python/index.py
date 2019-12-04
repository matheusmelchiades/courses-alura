from flask import Flask, render_template, request

app = Flask(__name__)



class Game:
    def __init__(self, name, className, console):
        self.name = name
        self.className = className
        self.console = console

listGames = [
    Game('Super Mario', 'Ação', 'Super nintendo'),
    Game('Pokemon Gold', 'RPG', 'GBA')
]

@app.route('/')
def index():
    return render_template('list.html', title='Games', games=listGames)


@app.route('/form')
def formGame(): 
    return render_template('form.html', title='New Game')


@app.route('/game', methods=['POST'])
def newGame():
    name = request.form['name']
    className = request.form['className']
    console = request.form['console']

    listGames.append(Game(name, className, console))

    return index()

app.run(debug=True)
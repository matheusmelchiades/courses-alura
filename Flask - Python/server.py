from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'python_test'


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
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect('/login?next=new')

    return render_template('form.html', title='New Game')


@app.route('/game', methods=['POST'])
def newGame():
    name = request.form['name']
    className = request.form['className']
    console = request.form['console']

    listGames.append(Game(name, className, console))

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def auth():
    password = request.form['password']

    if password == 'qwer1234':
        session['user_logged'] = request.form['username']
        flash(request.form['username'] + ' Logged with success!')
        path_redirection = '/'
    else:
        flash('User unauthorized!')
        path_redirection = '/login'
    return redirect(path_redirection)


@app.route('/logout')
def logout():
    session['user_logged'] = None
    flash('Nobody user logged!')
    return redirect('/')


app.run(debug=True)

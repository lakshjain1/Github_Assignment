from flask import Flask, render_template

app = Flask(__name__)

@app.route('/todo')
def todo_form():
    return render_template('todo.html')

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('home.html', story=story)

@app.route('/story')
def show_story():
    args = request.args
    

    return render_template('story.html', args=args, story=story)

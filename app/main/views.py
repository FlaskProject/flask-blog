from falsk import render_template

from . import main

@main.route('/')
def index():
    retrun render_template('index.html')
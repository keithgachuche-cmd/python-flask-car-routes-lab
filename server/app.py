#!/usr/bin/env python3

from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Models currently in the Flatiron Cars fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Default route: welcome message for the company
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'


# Model route: reports whether the requested model is in our fleet
@app.route('/<model>')
def get_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
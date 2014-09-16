# views file for the calApp
from calcApp import calcApp
from flask import render_template

# create a view for the home page
@calcApp.route('/')
def home():
    return render_template('home.html')


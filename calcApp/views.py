# views file for the calApp
from calcApp import calcApp
from flask import render_template
from flask import request

# function to convert percentage entered
def convert_tip_percentage(tip):
    conv_tip = float(tip)
    return conv_tip / 100.0

# create a view for the home page
@calcApp.route('/')
def home():

    return render_template('home.html')

@calcApp.route('/results', methods=['POST'])
def results():
    # create logic for calculating tip
    # set the value in meal_cost text field of the form to var
    meal_cost = float(request.form['meal_cost'])
    tip_percentage = convert_tip_percentage(request.form['tip_percentage'])
    tip_to_pay = meal_cost * tip_percentage
    tip_to_pay = "{:.2f}".format(tip_to_pay)
    # set the value tip_percentage text field to a value
    return render_template('results.html', tip=tip_to_pay)

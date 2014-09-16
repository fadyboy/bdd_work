# application init file for the calcApp

from flask import Flask

calcApp = Flask(__name__)

from calcApp import views


# Web Development With Python

# ###### How Websites Works ######

# As we can see in browsers(its a software that helps to surf internet through websites), Websites is just a three files (HTML, CSS, JS) that give us by server( it also a programme that written in programming language like Python, node js, php, java etc)
# so when we go browser and ask the browser hey i want google.com and browser ask the dns and dns says google comes from google server then dns request the google server to give me the google.com and it says sure here it is(Html, Css, JS)

# ######## How Websites Works 2 #######
# previously we see that browser send request server for website over the internet using HTTP/HTTPS protocols(set of rules) and receives the HTML, CSS, JS

#  for exactly see what happens behind the scenes
# 1. Open Chrome Browser
# 2. go to any particular website
# 3. open developer tools
# 4. go to network tab and refresh
#  see what data browser receives.


# #_#_#_# Flask #_#_#_#
# Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

# HTTP server= An HTTP server is software that understands URLs (web addresses) and HTTP (the protocol your browser uses to view webpages).

# ------------setting up a flask--------------
'''
1. create a project folder
2. create a virtual environment 
    a. python3 -m venv <foldername> or . (for using current folder)
3. activate virtual environment
    a. source <foldername>/bin/activate
4. install flask Framework from Pypi
    a. pip install Flask
'''

# ----------Building a Flask Server-------------
# basic minimal template
# from flask import Flask
# app = Flask(__name__) # __name__ is for that uses check out the file name
# @app.route('/') # decorator for routing the app on url, frameworks they give you higher level of abstraction.
# def hello_world():
#     return 'Hello World'

#  just thats pretty much it flask to run


# ----------running the Flask ----------
# for runnign the flask need to set the environment variable
# Go to terminal $ export FLASK_APP=<filename>
# flask run
# http://127.0.0.1:5000 (gave the localhost address with port 5000)

# turing on debug mode it gives the live changes option
# $ export FLASK_APP = development
# flask run


# -----------flask templating---------------
# this helps to render static files on browser

# from flask import Flask, render template
# --- -- - - - - - -
# --- -- - -- -

# @app.route('/about')
# def about():
#     return render_template('index.html')
# html files must be in templates folder

# --------static files-----------
# flask static files : the files that are never going to change and that is css and js files.
#  in flask need to create a static folder, move files in them

# ------------favicon-----------------
# favicon is the logo that place in header bar of browsers
# <link rel="shortcut icon"
# href="{{ url_for('static', filename='sign_notification_problem_alert_danger_attention_caution_exclamation_warning_icon_210746.ico') }}">


# ----------Template engine-------------

# it just way to sent dynamic data in html files using Jinja templating
# {{ <dynamic data }} this are the template language

# ---------------url_parameters------------
# @app.route('/<username>/<int:post_id>')
# def about(username=None, post_id=None):
#     # return render_template('index.html', name=username, post_id=post_id)
# that way we make dynamic urls

# ---------------MIME Type-------------
# Multipurpose Internet Mail Extensions(MIME)
# the idea behind mime type is server sends data to browser in a mime type format(content type) not a file extension format(index.html)
# if you go developer tools-> network : you seee a header of a file and in there a header that have multiple information related server and there a content/type: that shows the type of data, if its html file it shows text/html.
# further information go and check out here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types

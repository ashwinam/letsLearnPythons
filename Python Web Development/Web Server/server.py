from flask import Flask, render_template, url_for

app = Flask(__name__)  # main file


@app.route('/')
def hello_world():
    # print(url_for('static', filename='sign_notification_problem_alert_danger_attention_caution_exclamation_warning_icon_210746.ico')) # it gives the static path
    return 'Hello !!!!!'


@app.route('/blog')
def blog():
    return 'this page is about my thoughts.'

#  this way we can create url addreses


@app.route('/blog/2020/myDog1')
def blog2():
    return 'this page is  my dog.'

# render_template is helps to render the static files on browser
# static files must be in templates folder


@app.route('/<username>/<int:post_id>')
def about(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

# flask static files : the files that are never going to change and that is css and js files.
#  in flask need to create a static folder

# template engine

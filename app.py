from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/manpage')
# def manpage():
#     retrun render_template('manpage.html')

if __name__ == '__main__':
    app.run()

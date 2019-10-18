from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/manpage1')
def manpage1():
    return render_template('manpage.html')

@app.route('/manpage2')
def manpage2():
    return render_template('manpage_2.html')

@app.route('/manpage3')
def manpage3():
    return render_template('manpage_3.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()

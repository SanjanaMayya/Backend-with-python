from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    msg = '<h1> Hello %s! </h1>' % name
    msg += '<p> <i> Flask is a micro web framework writen in Python. </i> </p>'
    msg += '<p> Welcome to Flask! </p>'
    msg += '<p> Enjoy your stay. </p>'
    msg += '<p> Thanks for visiting! </p>'
    msg += '<p> Have a great day! </p>'
    return msg

if __name__ == '__main__':
    app.run()
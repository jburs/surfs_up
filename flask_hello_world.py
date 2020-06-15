#
#

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello world'



# in terminal: 
# $env:FLASK_APP=”app.py”
# flask run
# localhost:5000    in web browser

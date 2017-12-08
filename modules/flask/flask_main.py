"""
this module demonstrates basic features of base flask module
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello Flask'

if __name__ == '__main__':
	app.run()

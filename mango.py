from flask import Flask, render_template
from flask_bootstrap import Bootstrap 

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.errorhandler(404)
def page_not_foundd(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

bootstrap=Bootstrap(app)
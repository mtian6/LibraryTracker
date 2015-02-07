from flask import redirect, render_template, request, url_for
from run import app

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run()
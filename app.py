from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
	return render_template('new.html')

@app.route('/one')
def one():
	return render_template('one.html', foo=[1,2,3,4])

if __name__=='__main__':
	app.run(debug=True)

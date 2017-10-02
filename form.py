from flask import Flask, render_template, request 
app = Flask(__name__)

#,methods=['POST','GET'])


@app.route('/')
def index():
	return render_template('base.html')

@app.route('/echo')
def echo():
	return render_template('echo.html',input=request.args['input'],type=request.method)
	#return request.method


if __name__=='__main__':
	app.run(debug=True)
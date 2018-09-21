
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/blackwhite', methods=['POST'])
def blackwhite():
	if 'media' in request.files:
		return send_file(
			'input/bebek.jpg',
			mimetype='image/jpeg'
		)

@app.route('/', methods=['GET'])
def main():
	return 'Its Works!'

@app.route('/process', method=['POST'])
def process():
	imagefile = request.files.get('image', '')
	return send_file('input/bebk.jpg', mimetype='image/jpeg')

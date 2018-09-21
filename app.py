
from flask import Flask, send_file, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/blackwhite', methods=['POST'])
def blackwhite():
	if 'media' in request.files:
		return send_file(
			'input/nums.jpg',
			mimetype='image/jpeg'
		)

@app.route('/', methods=['GET'])
def main():
	return 'Its Works!'

@app.route('/process', methods=['POST'])
def process():
	imagefile = request.files.get('image', '')
	resp = send_file('input/nums.jpg', mimetype='image/jpeg')
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

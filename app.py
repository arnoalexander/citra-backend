
from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/blackwhite', methods=['POST'])
def blackwhite():
	if 'media' in request.files:
		return send_file(
			'bebek.jpg',
			mimetype='image/jpeg'
		)

@app.route('/', methods=['GET'])
def main():
	return 'Its Works!'
from flask import Flask, render_template
import glob, os
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/js_request')
def verses():
	return reading_detection_data()

def reading_detection_data():
	detection_array = []
	for file in glob.glob("*.txt"):
		while True:
			try:
				read_from_file_path = file
				output_file = open(read_from_file_path, "r")
				line = output_file.read()
				output_file.close()
			except Exception as e:
				continue
			else:
				detection_array.append(line)
				break
	detection_json = json.dumps(detection_array)
	return detection_json
	
	

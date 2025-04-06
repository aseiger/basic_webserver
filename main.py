#!/bin/bash
from flask import Flask, Response, request, jsonify, render_template, send_from_directory
import os

# This application runs an extremely bare-bones HTTP serve. It serves up a single HTML page
# with no static file support. Flask has a whole templating engine that is completely bypassed here.
# 
# The intent is that this app can be used as a starting point for creating basic user interfaces surrounding
# physical hardware.
#
# Access the UI by going to localhost:8080

app = Flask("MainTester")


# Show the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Main page
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

# Example API endpoint for set_load
@app.route('/set_load', methods=['POST'])
def set_load():
    if request.is_json:
        data = request.get_json()
        load_lbs = data.get('load_lbs')

        if load_lbs:
            response = {'message': 'Data received successfully', 'load_lbs': load_lbs}

            # TODO set load here via call to serial

            print("Setting Load to {:f}".format(load_lbs))
            return jsonify(response), 200 # Return JSON response with status code 200 (Success)
        else:
            return jsonify({'error': 'Missing name or email in JSON data'}), 400 # Bad request
    else:
        return jsonify({'error': 'Request data must be in JSON format'}), 400


if __name__ == "__main__":
    # TODO Serial Initialization here
    app.run(port=8080, debug=True)
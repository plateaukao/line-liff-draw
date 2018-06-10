from flask import Flask, request, render_template, make_response,jsonify 
from flask_bootstrap import Bootstrap

import os
import uuid
import base64
import giphy

app = Flask(__name__, static_folder='imgs')
bootstrap = Bootstrap(app)

@app.route('/')
def page_giphy():
    return render_template('giphy.html')

@app.route('/api/giphy/search', methods=['GET'])
def giphylist():
    url_list = giphy.query(request.args.get('keyword'))
    result = {'urls': url_list}
    return make_response(jsonify(result), 200)

if __name__ == '__main__':
    app.debug = True
    app.run()

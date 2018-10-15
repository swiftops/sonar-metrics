import logging
from flask import Flask, request
import json
from sonarmethod import getsonarmetrics

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
@app.route('/sonarfilter', methods=['POST'])
def sonarfilter():
    #query = request.data.decode()
    query = json.loads(request.data.decode())
    projectkey = query.split(';')[1]
    return getsonarmetrics(projectkey)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7975, debug=True)

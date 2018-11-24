
import json
from flask import Flask
import KeyWordExtractor as kwe
app = Flask(__name__)

extractor = kwe.KeyWordExtractor()

@app.route("/getKeywords/<id>")
def getKeywords(id):
    return json.dumps(extractor.extractKeywords(id))


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)

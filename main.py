
import json
from flask import Flask
import KeyWordExtractor as kwe
app = Flask(__name__)

extractor = kwe.KeyWordExtractor()


@app.route("/getKeywords/<id>")
def getKeywords(id):
    return json.dumps(extractor.extractKeywords(id))


@app.route("/generateMotivation/<keyword>/<score>")
def motivationGenerator(keyword, score):
    motivation = {"message":""}
    score = int(score)
    if score < 9:
        motivation["message"] = "Denied allowance because of good: {}".format(keyword)
    elif score >= 9 and score < 19:
        motivation["message"] = "Granted allowance because of bad: {}".format(keyword)
    else:
        motivation["message"] = "Score out of bounds"

    return json.dumps(motivation)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)

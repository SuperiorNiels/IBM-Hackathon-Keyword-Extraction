
import json
from PdfToText import PdfToText
import requests
import os


class KeyWordExtractor:
    url = "https://gateway-fra.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-09-21"
    api = ('apikey', '0ZSNUotlfdYdVz8U2udrbgPVhdv7nK5PH1q2c-i2Q-oa')
    headers = {'Content-type': 'application/json'}
    data = json.loads(open('parameters.json').read())

    path = "./patients/"        # base path (where the patient folders need to be)

    def getKeywords(self,text):
        self.data["text"] = text
        response = requests.post(self.url, data=json.dumps(self.data), headers=self.headers, auth=self.api).json()
        if "entities" in response:
            return response["entities"]
        return []


    def printKeywords(self,keywords):
        for keyword in keywords:
            print("%s \n\t type: %s" % (keyword["text"],keyword["type"]))

    def extractKeywords(self,patientID):
        path = self.path + "patient" + patientID + "/"
        files = os.listdir(path)
        print("Loading %d files." % len(files))
        result = {"keywords": []}
        for file in files:
            if file.endswith(".pdf"):
                pdfToText = PdfToText(path+file)
                text = pdfToText.getText()
                for word in self.getKeywords(text):
                    result["keywords"].append({
                        "text": word["text"],
                        "type": word["type"],
                        "file": file}
                    )
            elif file.endswith(".txt"):
                try:
                    text = open(path+file).read()
                    for word in self.getKeywords(text):
                        result["keywords"].append({
                            "text": word["text"],
                            "type": word["type"],
                            "file": file}
                        )
                except UnicodeDecodeError:
                    print("File %s decode error." % path+file)
        return result






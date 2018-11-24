
import PyPDF2

class PdfToText:

    def __init__(self,filename):
        self.setFilename(filename)

    def getText(self):
        pdfFileObj = open(self.filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        input = ""
        for i in range(pdfReader.getNumPages()):
            pageObj = pdfReader.getPage(i)
            input += pageObj.extractText()
        return input

    def setFilename(self,filename):
        self.filename = filename

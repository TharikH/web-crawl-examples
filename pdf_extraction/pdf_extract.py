import PyPDF2
import re
def extract(mypdf):
    mypdf=open(mypdf,"rb") #open pdf
    pdfread=PyPDF2.PdfFileReader(mypdf)#read pdf

    arr=[]  #initializing list to store links

    for i in range(pdfread.numPages):
        page=pdfread.getPage(i) #taking each page
        url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',page.extractText())
        arr.append(url) #taking each page's url into array
    return arr
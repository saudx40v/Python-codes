#Extracting Text From PDF with Python
# first we install pyPDF2 in Terminal
# pip install pypdf2 


import PyPDF2
pdf = open("Aman.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())
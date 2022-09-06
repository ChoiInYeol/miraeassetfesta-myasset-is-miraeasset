# pip install PyPDF2
# pip install PDFFileReader
# pip install pdf

import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

filename = "NH투자증권.pdf"
filepath = os.path.join(os.getcwd(),filename)

# PDF의 Total 페이지를 읽어오기 
fp = open(filepath, 'rb')
total_pages = PyPDF2.PdfFileReader(fp).numPages

# pdfminer로 페이지별 텍스트 가져오기 
page_text = {}
for page_no in range(total_pages):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    device = TextConverter(rsrcmgr, retstr, laparams=LAParams())
    fb = open(filepath, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    caching = True
    maxpages = 0
    pagenos = [page_no]
    for page in PDFPage.get_pages(fb, pagenos, maxpages = maxpages, 
                              caching = caching, check_extractable = True):
        interpreter.process_page(page)
        page_text[page_no] = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()

# 원하는 페이지 첫번째 []에 입력 
# 1 page 내용 출력
print(page_text[1][:-1])
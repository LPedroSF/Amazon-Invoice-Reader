from pypdf import PdfReader 
import re
import os

dir_list = os.listdir(os.getcwd())

pdfs= []
strings = []
total = 0

for file in dir_list:
  if file.endswith(".pdf"):
    reader = PdfReader(file) 
    page = reader.pages[0]  
    text = page.extract_text() 
    index = text.find("Total payable ")
    new_text = text[index:index + 30]
    pdfs.append(new_text)

for i in pdfs:
  x = re.findall("\d+\.\d+",i)
  strings.append(x[0])

for j in range (0, len(strings)):
  total += float(strings[j])  

print()
print("The total amount for the invoices: ",round(total, 2))
print()
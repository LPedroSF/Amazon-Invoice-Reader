from pypdf import PdfReader 
import re
import os

#get the current dirtectory path
dir_list = os.listdir(os.getcwd())
total = 0

def addInvoices():
  global total
  #search all invoices and adds all prices to a list
  for file in dir_list:
    if file.endswith(".pdf"):
      #find the price
      reader = PdfReader(file) 
      page = reader.pages[0]  
      text = page.extract_text() 
      index = text.find("Total payable ")
      new_text = text[index:index + 30]
      x = re.findall("\d+\.\d+",new_text)

      #convert it to float from string
      num = float(x[0])
      total += num

  return total



print()
print()
print("The total amount of the invoices is: ", addInvoices())
print()
print()
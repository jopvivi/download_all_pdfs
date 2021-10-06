import re

PDFList = []
with open('input.txt', 'r', encoding='UTF-8') as file:
    fileList = file.readlines() # Reads the file, line by line into a list.
    squash = ' '.join(fileList).replace('\n','') # Squashes everything together, removing spaces and returns.
    urls = re.findall(r'(https?://\S+)', squash) # Digs through the squashed mess, pulling out all 'https' links
    for i in urls: # Iterate thru the links
        if "pdf" in i: # Test if the link contains the string 'pdf'
            if i.endswith('.') == True: # Cleans the results a bit
                i = (i[:-1])
            if i.endswith(';') == True: # Cleans the results a bit
                i = (i[:-1])
            PDFList.append(i)

for pdf in PDFList:
    print(pdf)
print('There are ' + str(len(PDFList)) + ' PDFs in the file.')


from contextlib import redirect_stdout # Redirects the output to a file

with open('out.txt', 'w') as f:
    with redirect_stdout(f):
        for pdf in PDFList:
            print(pdf)

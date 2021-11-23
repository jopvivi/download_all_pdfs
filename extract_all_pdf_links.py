import glob
import re

pdf_list = []
file_pattern = '*.txt'
file_name_list = []

if '*' in file_pattern:
    file_name_list.extend(glob.glob(file_pattern))

for target in file_name_list:
    with open(target, 'r', encoding='UTF-8') as file:
        file_list = file.readlines() # reads the file, line by line into a list
        squash = ' '.join(file_list).replace('\n','') # squashes everything together, removing spaces and returns
        urls = re.findall(r'(https?://\S+)', squash) # digs through the squashed mess, finds all 'https' links
        for i in urls: # iterates through the links
            if "pdf" in i: # tests if the link contains the string 'pdf'
                if i.endswith('.'): # cleans the results a bit
                    i = (i[:-1])
                if i.endswith(';'): # cleans the results a bit
                    i = (i[:-1])
                pdf_list.append(i)

for pdf in pdf_list:
    print(pdf)
print('There are ' + str(len(pdf_list)) + ' PDFs in the file(s).')

from contextlib import redirect_stdout # redirects the output to a file

with open('pdfs_links.txt', 'w') as f:
    with redirect_stdout(f):
        for pdf in pdf_list:
            print(pdf)

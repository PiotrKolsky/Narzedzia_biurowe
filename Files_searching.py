
import PyPDF2
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import os

def search_pdfs(dir_name, type = '.pdf'):
    files_list = list()
    for (dirpath, dirnames, filenames) in os.walk(dir_name):
        for file in filenames:
            if file.endswith(type):
                files_list += [os.path.join(dirpath, file)]
    return files_list

def search_in_pdf(filename, key):
    key = key.lower().strip()
    occurrences = 0
    pages_num = []
    punctuation = ['(',')',';',':','[',']',',','-']
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    num_pages = pdf_reader.numPages
    count = 0
    text = ''
    while count < num_pages:
        page_obj = pdf_reader.getPage(count)
        count +=1
        text = page_obj.extractText()
        if text != '':
           text = text.lower()
        else:
            pass
        tokens = word_tokenize(text)
        keywords = [word for word in tokens if not word in punctuation]
        for k in keywords:
            if key == k:
                occurrences+=1
                pages_num.append(count)
    return occurrences, np.sort(list(set(pages_num)))

path = '/home/sas/Zasoby/Python/Test'

files_list = search_pdfs(path, '.pdf')

search_for = 'Logger'

df = pd.DataFrame(columns=['file','word','occurrences', 'pages'])

for file in files_list:
    (occurr, pages) = search_in_pdf(file, search_for)
    df_temp = pd.DataFrame({'file':[file], 'word':[search_for.lower()], 'occurrences':[occurr],'pages': [pages] })
    df = df.append(df_temp)
df = df.reset_index(drop=True)

dest_filename = (path + '/words_found.xlsx')
df.to_excel(dest_filename, index=True)
#####################################

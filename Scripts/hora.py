import PyPDF2
import re
import os

regex_time = r"\b\d{2}:\d{2}\b"
folder_path = r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\parserGobierno\Archivos\PDF'

before_words_list = []

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                lines = page_text.split("\n")
                for line in lines:
                    matches = re.finditer(regex_time, line)
                    for match in matches:
                        start_index = match.start()
                        if start_index > 0:
                            before_word = line[start_index - 1]
                            before_words_list.append(before_word)

print("Palabras anteriores a la hora encontradas en los documentos PDF:")
for word in before_words_list:
    print(word)

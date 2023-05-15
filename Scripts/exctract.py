#1 y 6
#3, 4, 14 y 16
import PyPDF2
import re
import os

regex = r"\d{2}/\d{2}/\d{2}\s+\d{2}/\d{2}/\d{2}"
regex_country = r"\b(CHINA|MEXICO|MÉXICO)\b"

folder_path = r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\parserGobierno\Archivos\PDF'

result_values = []
countries_list = []

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page = pdf_reader.pages[0]
            page_text = page.extract_text()
            matches = re.findall(regex, page_text)
            countries = re.findall(regex_country, page_text)
            if countries:
                countries_list.extend(countries)
            for match in matches:
                line = re.search(r'(^.*?{}.*?$)'.format(match), page_text, re.MULTILINE)
                if line:
                    result_values.append(line.group().strip())

for i in range(len(result_values)):
    result_values[i] = result_values[i].split()

transposed = list(zip(*result_values))
lote_03 = transposed[0]
caducidad_04 = transposed[1]
fechaFabr_14 = transposed[2]
paisOrigen_16 = countries_list


print(lote_03)
print(caducidad_04)
print(fechaFabr_14)
print(countries_list)
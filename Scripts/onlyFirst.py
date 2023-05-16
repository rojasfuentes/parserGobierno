#3, 4, 14 y 16
import PyPDF2
import re
import os
from datetime import datetime

regex = r"\d{2}/\d{2}/\d{2}\s+\d{2}/\d{2}/\d{2}"
regex_country = r"\b(CHINA|(?!CIUDAD\s+DE\s+|ESTADO\s+DE\s+)MÉXICO|(?!CIUDAD\s+DE\s+|ESTADO\s+DE\s+)MEXICO)\b"

folder_path = r'C:\Users\JFROJAS\Desktop\Gobierno\Archivos\PDF'
result_values = []
countries_list = []
caducidad_04 = []
fechaFabr_14 = []
sumElementos = []

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
    sumElementos.append(len(result_values))

for i in range(len(result_values)):
    result_values[i] = result_values[i].split()

noElementos = []
for i in range(len(sumElementos)):
    if i == 0:
        noElementos.append(sumElementos[i])
    else: 
        noElementos.append(sumElementos[i] - sumElementos[i-1])

transposed = list(zip(*result_values))
lote_03 = transposed[0]
caducidad = transposed[1]
fechaFabr = transposed[2]
paisOrigen_16 = countries_list

#4 y 14


for fecha in caducidad:
    fecha_datetime = datetime.strptime(fecha, '%d/%m/%y')
    nueva_fecha = fecha_datetime.strftime('%Y%m%d')
    caducidad_04.append(nueva_fecha)


for fecha in fechaFabr:
    fecha_datetime = datetime.strptime(fecha, '%d/%m/%y')
    nueva_fecha = fecha_datetime.strftime('%Y%m%d')
    fechaFabr_14.append(nueva_fecha)



#print(lote_03)
#print(caducidad_04)
#print(fechaFabr_14)
#print(paisOrigen_16)




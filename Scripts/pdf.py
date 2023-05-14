import os
import PyPDF2
import re

# regex para la búsqueda original
regex_suministro = r'SUMINISTRO\s+(\S[^\r\n]*)'

# regex para la nueva búsqueda
regex_puntos = r'\b\S+\.\S+\.\S+\b'

folder_path = r'C:\Users\Frida Colin\Desktop\GobGuapo\parserGobierno\Archivos\PDF'

result_values = []
result_values_2 = []

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            last_match = None
            last_match_2 = None
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                
                # búsqueda original
                matches = re.finditer(regex_suministro, page_text, re.IGNORECASE)
                for matchNum, match in enumerate(matches, start=1):
                    last_match = match.group(1).strip()
                
                # nueva búsqueda
                matches_2 = re.finditer(regex_puntos, page_text, re.IGNORECASE)
                for matchNum, match in enumerate(matches_2, start=1):
                    last_match_2 = match.group().strip()
                
            if last_match:
                result_values.append(last_match.split())
            if last_match_2:
                result_values_2.append(last_match_2)

#1 y 6
transposed = list(zip(*result_values))
noRemision_01 = transposed[0]
noOrdRep_06 = transposed[1]


#2
sinLetras = r'[^0-9\.]'
for i in range(len(result_values_2)):
    result_values_2[i] = re.sub(sinLetras, '', result_values_2[i])
codigoProd_02 = result_values_2


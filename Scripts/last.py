#1, 2 , 6, 7, 18, 19 y 20
import os
import PyPDF2
import re

# regex para la búsqueda original
regex_suministro = r'SUMINISTRO\s+(\S[^\r\n]*)'
regex_state = r'\(CLUES\):\s+(\S[^\r\n]*)'
regex_destino = r'CLUES:\s+(\S[^\r\n]*)'
regex_destino2 = r'CLUES:+(\S[^\r\n]*)'
regex_total = r'Total\s+(\S[^\r\n]*)'
regex_total2 = r'tarimas\s+(\S[^\r\n]*)'

# regex para la nueva búsqueda
regex_puntos = r'\b\S+\.\S+\.\S+\b'

folder_path = r'C:\Users\JFROJAS\Desktop\Gobierno\Archivos\PDF'

result_values = []
result_values_2 = []
result_total = []
entidadFed_20 = []
destino_18 = []

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            last_match = None
            last_match_2 = None
            last_state_match = None
            last_destino_match = None
            last_total_match = None
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

                state_match = re.finditer(regex_state, page_text, re.IGNORECASE)
                for matchNum, match in enumerate(state_match, start=1):
                    last_state_match = match.group(1).strip()
                
                total_match = re.finditer(regex_total, page_text, re.IGNORECASE)
                for matchNum, match in enumerate(total_match, start=1):
                    last_total_match = match.group(1).strip()
                    if last_total_match == 'tarimas':
                        total_match_2 = re.finditer(regex_total2, page_text, re.IGNORECASE)
                        for matchNum, match in enumerate(total_match_2, start=1):
                            last_total_match = match.group(1).strip()
                
                destino_match = re.findall(regex_destino, page_text, re.IGNORECASE)
                destino_match = destino_match + re.findall(regex_destino2, page_text, re.IGNORECASE)
                if destino_match:
                    last_destino_match = destino_match[0].strip()
                    destino_18.append(last_destino_match)
                
            if last_match:
                result_values.append(last_match.split())
            if last_match_2:
                result_values_2.append(last_match_2)
            if last_state_match:
                entidadFed_20.append(last_state_match.split())
            if last_total_match:
                result_total.append(last_total_match.split())
            

#1 y 6
transposed = list(zip(*result_values))
noRemision_01 = transposed[0]
noOrdRep_06 = transposed[1]

#18
for i in range(len(destino_18)):
    destino_18[i] = destino_18[i].split()
for i in range(len(destino_18)):
    destino_18[i] = destino_18[i][0]

#7 y 19
transposedTotal = list(zip(*result_total))
noContrato_07 = transposedTotal[0]
licitacion_19 = transposedTotal[1]

#20
for i in range(len(entidadFed_20)):
    entidadFed_20[i] = entidadFed_20[i][0]

# La linea anterior imprime



#2
sinLetras = r'[^0-9\.]'
for i in range(len(result_values_2)):
    result_values_2[i] = re.sub(sinLetras, '', result_values_2[i])
codigoProd_02 = result_values_2

#print(noRemision_01)
#print(codigoProd_02)
#print(noOrdRep_06)
#print(noContrato_07)
#print(destino_18)
#print(licitacion_19)
#print(entidadFed_20)

import PyPDF2
import re
import os

regex = r"\d{2}/\d{2}/\d{2}\s+\d{2}/\d{2}/\d{2}"
regex_country = r"\b(CHINA|MEXICO|MÉXICO)\b"

folder_path = r'C:\Users\Frida Colin\Desktop\GobGuapo\parserGobierno\Archivos\PDF'

result_values = []
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)  
            page = pdf_reader.pages[0]
            page_text = page.extract_text()
            matches = re.findall(regex, page_text)
            countries = re.findall(regex_country, page_text)
            if countries:
                print(countries)
                for country in countries:
                    country_positions = [m.start() for m in re.finditer(country, page_text)]
                    for pos in country_positions:
                        before = page_text[:pos]
                        after = page_text[pos+len(country):]
                        before_words = before.split()
                        after_words = after.split()
                        if before_words:
                            print("Anterior a {}: {}".format(country, before_words[-1]))
                        if after_words:
                            print("Siguiente a {}: {}".format(country, after_words[0]))
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

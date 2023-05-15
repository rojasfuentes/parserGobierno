import PyPDF2
import re
import os

regex_country = r"\b(CHINA|MEXICO|MÉXICO)\b"

folder_path = r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\parserGobierno\Archivos\PDF'

countries_list = []
before_words_list = []
after_words_list = []

for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page = pdf_reader.pages[0]
            page_text = page.extract_text()
            countries = re.findall(regex_country, page_text)
            if countries:
                for country in countries:
                    if country not in countries_list:
                        countries_list.append(country)
                        country_positions = [m.start() for m in re.finditer(country, page_text)]
                        for pos in country_positions:
                            before = page_text[:pos]
                            after = page_text[pos + len(country):]
                            before_words = before.split()
                            after_words = after.split()
                            if before_words:
                                before_words_list.append(before_words[-1])
                            if after_words:
                                after_words_list.append(after_words[0])

marca_17 = [re.sub(r'\d', '', word) if re.search(r'\d', word) else word for word in before_words_list]
cantidad_05 = after_words_list


print(marca_17)
print(cantidad_05)



# 5 , 12 , 13 , 17
import PyPDF2
import re
import os
from datetime import datetime

#country_options = "Canada|Mexico|United States|Afghanistan|Albania|Algeria|American Samoa|Andorra|Angola|Anguilla|Central African Republic|Antigua & Barbuda|Argentina|Armenia|Aruba|Australia|Austria|Azerbaijan|Bahamas|Bahrain|Bangladesh|Barbados|Belarus|Belgium|Belize|Benin|Bermuda|Bhutan|Bolivia|Bosnia and Herzegowina|Botswana|Italia|Brasil|Brunei Darussalam|Bulgaria|Burkina Faso|Burundi|Cambodia|Cameroon|Cape Verde|Chad|Chile|China|Colombia|Congo|Cook Islands|Costa Rica|Croatia|Cuba|Chipre|Czech Republic|Denmark|Djibouti|Dominica|Dominican Republic|East Timor|Ecuador|Egipto|El Salvador|Eritrea|Estonia|Ethiopia|Faeroe Islands|Falkland Islands|Fiji|Finland|France|French Guiana|French Polynesia|Gabon|Gambia|Georgia|Alemania|Ghana|Gibralter|Greece|Greenland|Grenada|Guadeloupe|Guam|Guatemala|Guinea|Guinea-Bissau|Guyana|Haiti|Honduras|Hong Kong|Hungary|India|Indonesia|Iraq|Ireland|Israel|Jamaica|Japan|Jordan|Kazakstan|Kenya|Kiribati|Korea, Democratic People's Rep|Korea, Republic of|Kuwait|Kyrgystan|Lao People's Democratic Republ|Latvia|Lebanon|Lesotho|Liberia|Libyan Arab Jamahiriya|Liechtenstein|Lithuania|Luxembourg|Macau|Macedonia (FYROM|Madagascar|Malawi|Malaysia|Maldives|Mali|Malta|Marshall Islands|Martinique|Mauritania|Mauritius|Micronesia|Moldova|Monaco|Mongolia|Montserrat|Morocco|Mozambique|Myanmar|Namibia|Nauru|Nepal|Netherlands|Netherlands Antilles|New Caledonia|New Zealand|Nicaragua|Niger|Nigeria|Norfolk Island|Northern Mariana Islands|Norway|Oman|Pakistan|Palau|Panama|Papua New Guinea|Paraguay|Peru|Philippines|Pitcairn|Poland|Portugal|Puerto Rico|Qatar|Reunion|Romania|Russian Federation|Rwanda|Saint Lucia|Saint Vincent and the Grenadin|Samoa|San Marino|Sao Tome and Principe|Saudi Arabia|Senegal|Seychelles|Sierra Leone|Singapore|Slovenia|Comoros|Solomon Islands|Somalia|South Africa|Zaire|España|Sri Lanka|St. Helena|St. Kitts and Nevis|St. Pierre and Miquelon|Sudan|Suriname|Suecia|Swaziland|Suiza|Syrian Arab Republic|Taiwan, Province of China|Tajikistan|Tanzania|Thailand|Togo|Tonga|Trinidad and Tobago|Tunisia|Turkey|Turkmenistan|Turks and Caicos Islands|Tuvalu|Uganda|Ukraine|United Arab Emirates|Reino Unido|Uruguay|Uzbekistan|Vanuatu|Vatican City State|Venezuela|Vietnam|Virgin Islands, British|Virgin Islands, U.S|Wallis and Futuna Islands|Yemen|Yugoslavia|Zambia|Zimbabwe|Iceland|Iran|Cayman Islands|Ivory Coast|Wake Island|Inglaterra|"

regex_country = r"\b(CHINA|MEXICO|MÉXICO)\b"
regex_date = r"\d{2}/\d{2}/\d{4}"
regex_hora = r'\b\d{2}:\d{2}\b'


folder_path = r'C:\Users\JFROJAS\Desktop\Gobierno\Archivos\PDF'

countries_list = []
before_words_list = []
after_words_list = []
hour_list = []
hour_before_list = []
fechaEmision_12 = []
fechaEntrega_13 = []


for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page = pdf_reader.pages[0]
            page_text = page.extract_text()
            countries = re.findall(regex_country, page_text)
            hours = re.findall(regex_hora, page_text)
            datematch = re.findall(regex_date, page_text)
            if datematch:
                fechaEmision_12.extend(datematch)
            if hours:
                for hour in hours:
                    if hour not in hour_list:
                        hour_list.append(hour)
                        hour_positions = [m.start() for m in re.finditer(hour, page_text)]
                        for pos in hour_positions:
                            before = page_text[:pos]
                            before_words = before.split()
                            if before_words:
                                hour_before_list.append(before_words[-1])

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




for fecha in hour_before_list:
    fecha_converted = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y%m%d')
    fechaEntrega_13.append(fecha_converted)

for fecha in fechaEmision_12:
    fecha_converted = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y%m%d')
    fechaEmision_12[fechaEmision_12.index(fecha)] = fecha_converted

for elemento in fechaEntrega_13:
    if elemento in fechaEmision_12:
        fechaEmision_12.remove(elemento)

#print(cantidad_05)
#print(fechaEmision_12)
#print(fechaEntrega_13)
#print(marca_17)

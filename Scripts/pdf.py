import os
import PyPDF2
import re

# Definir la expresión regular para buscar el texto después de la palabra "SUMINISTRO:"
regex = r'SUMINISTRO:\s+([^\n]+)'

# Recorrer todos los archivos PDF en la carpeta
folder_path = r'C:\Users\JFROJAS\Desktop\Gobierno\Archivos\PDF'

# Abrir el archivo de texto donde se guardarán los resultados
with open('resultados.txt', 'w') as output_file:

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            # Abrir el archivo PDF en modo lectura binaria
            with open(os.path.join(folder_path, filename), 'rb') as pdf_file:
                # Crear un objeto PdfReader
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Obtener el número de páginas del archivo PDF
                num_pages = len(pdf_reader.pages)

                # Recorrer todas las páginas del archivo PDF
                for page_number in range(num_pages):
                    # Obtener la página actual del archivo PDF
                    page = pdf_reader.pages[page_number]

                    # Obtener el contenido de la página actual
                    page_content = page.extract_text()

                    # Buscar el texto después de la palabra "SUMINISTRO:" en el contenido de la página actual
                    matches = re.findall(regex, page_content)

                    if matches:
                        # Si se encontró una coincidencia, obtener la línea siguiente
                        next_line_regex = re.compile(r'SUMINISTRO:\s+[^\n]+\n(.+)')
                        next_line_matches = next_line_regex.findall(page_content)

                        if next_line_matches:
                            next_line = next_line_matches[0]
                            # Guardar el contenido en el archivo de texto
                            output_file.write(f"Archivo: {filename}, Página: {page_number+1}, Renglón siguiente: {next_line}\n")
                        else:
                            output_file.write(f"Archivo: {filename}, Página: {page_number+1}, No se encontró el siguiente renglón después de 'SUMINISTRO:'\n")
                    else:
                        output_file.write(f"Archivo: {filename}, Página: {page_number+1}, No se encontró 'SUMINISTRO:' en la página\n")

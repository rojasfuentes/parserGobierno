import PyPDF2

with open(r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\parserGobierno\Archivos\PDF\INSABI ejemplo 1.pdf', 'rb') as pdf_file:
    
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    with open(r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\Parser\parserGobierno\contenido.txt', 'w', encoding='utf-8') as text_file:
        # Iterar sobre cada página del PDF
        for page_num in range(len(pdf_reader.pages)):
            #página actual
            page = pdf_reader.pages[page_num]

            # Extraer el texto de la página actual
            page_text = page.extract_text()
            text_file.write(page_text)

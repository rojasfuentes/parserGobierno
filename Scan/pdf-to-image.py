import os
from pdf2image import convert_from_path

poppler_path = r'C:/Users/JFROJAS/Downloads/poppler-0.68.0_x86/poppler-0.68.0/bin'
os.environ['PATH'] += os.pathsep + poppler_path

folder_path = r'C:\Users\JFROJAS\Desktop\Gobierno\Archivos\Scanner'

# Crea la carpeta "output" si no existe
output_folder = os.path.join(folder_path, 'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
files = os.listdir(folder_path)


pdf_files = [file for file in files if file.endswith('.pdf')]


for i, pdf_file in enumerate(pdf_files):
    pdf_path = os.path.join(folder_path, pdf_file)
    pages = convert_from_path(pdf_path)
    for j, page in enumerate(pages):
        output_file = os.path.join(output_folder, f'pagina_{i}_{j}.jpg')
        page.save(output_file, 'JPEG')

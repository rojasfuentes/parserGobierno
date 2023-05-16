import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/imghp")

print("Google Images opened")


folder = r"C:\Users\JFROJAS\Desktop\Gobierno\Archivos\Scanner\output"
output_folder = r"C:\Users\JFROJAS\Desktop\Gobierno\Archivos\Scanner\output"


for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        time.sleep(2)
        filepath = os.path.join(folder, filename)
        filepath = filepath.replace("/", "\\")
        # Seleccionar la opción de "Buscar por imagen" nDcEnd
        search_by_image_button = driver.find_element(by='class name', value='nDcEnd')
        search_by_image_button.click()
        print("Search by image button clicked")
    
        search_input = driver.find_element(by='class name', value='cB9M7')
        search_upload = driver.find_element(by='class name', value='DV7the')
        search_upload.click()
        time.sleep(1)
        pyautogui.typewrite(filepath, interval=0.001) 
        pyautogui.press('enter')
        print("File uploaded")
        time.sleep(5)
        pyautogui.click(270, 930)
        print("Tex button clicked")
        time.sleep(3)
        pyautogui.click(750, 720)
        time.sleep(3)
        pyautogui.click(600, 310)
        time.sleep(2)

        # Obtener el texto del portapapeles
        text_to_append = pyperclip.paste()
        
        output_file_path = os.path.join(folder, "texto.txt")

        # Abrir el archivo en modo de escritura y agregar el texto al final
        with open(output_file_path, "a", encoding='utf-8') as f:
            f.write(text_to_append)

        driver.get("https://www.google.com/imghp")

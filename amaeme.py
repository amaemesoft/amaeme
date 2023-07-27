"""
    AMAEME: Un asistente de mensajería anónima y extractor de mensajería encriptada

    Copyright (C) 2023  AmaEmeSoft

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import stepic
import threading
import os
from cryptography.fernet import Fernet
import logging

# Configuración del registro de eventos
logging.basicConfig(filename="registro.log", level=logging.INFO, format='%(asctime)s %(message)s')

# Clave de cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def incluir_mensaje():
    file_path = filedialog.askopenfilename(filetypes=(("Archivos JPEG", "*.jpeg"), ("Archivos PNG", "*.png"), ("Archivos BMP", "*.bmp"), ("Todos los archivos", "*.*")))
    if not file_path:
        return
    img = Image.open(file_path)
    message = entrada_texto.get("1.0", "end-1c")
    if not message:  # Comprobar si el mensaje está vacío
        messagebox.showerror("Craso error", "No has introducido texto, lol.")
        logging.error("Intento de incluir mensaje vacío")
        return

    # Encriptar el mensaje
    message_bytes = cipher_suite.encrypt(message.encode())
    logging.info("Mensaje encriptado")

    img_with_message = stepic.encode(img, message_bytes)
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    if save_path:
        img_with_message.save(save_path, "PNG")
        logging.info(f"Imagen guardada en {save_path}")

        # Guardar la clave en el mismo directorio que la imagen con el mismo nombre que la imagen "estenografiada"
        key_save_path = os.path.splitext(save_path)[0] + ".key"
        with open(key_save_path, "wb") as key_file:
            key_file.write(key)
        logging.info(f"Clave guardada en {key_save_path}")

    # Mostrar el mensaje sin cifrar durante dos segunditos
    entrada_texto.delete("1.0", tk.END)
    entrada_texto.insert(tk.END, message)
    window.after(2000, lambda: entrada_texto.delete("1.0", tk.END))

    # Mostrar la versión encriptada del mensaje en la ventana después de que se borre el mensaje sin cifrar
    window.after(2000, lambda: entrada_texto.insert(tk.END, message_bytes.decode()))

    # Borrar el mensaje cifrado después de dos segunditos más
    window.after(4000, lambda: entrada_texto.delete("1.0", tk.END))

def extraer_mensaje():
    file_path = filedialog.askopenfilename(filetypes=(("Archivos JPEG", "*.jpeg"), ("Archivos PNG", "*.png"), ("Archivos BMP", "*.bmp"), ("Todos los archivos", "*.*")))
    if not file_path:
        return
    img = Image.open(file_path)
    logging.info(f"Imagen abierta desde {file_path}")

    # Extraer el mensaje oculto
    message_bytes = stepic.decode(img)
    logging.info("Mensaje oculto extraído")

    # Mostrar el mensaje cifrado durante 2 segundos 
    entrada_texto.delete("1.0", tk.END)
    entrada_texto.insert(tk.END, message_bytes)
    window.after(2000, lambda: entrada_texto.delete("1.0", tk.END))

    # Leer la clave del archivo .key correspondiente
    key_file_path = os.path.splitext(file_path)[0] + ".key"
    with open(key_file_path, "rb") as key_file:
        key = key_file.read()
        cipher_suite = Fernet(key)

    # Desencriptar el mensaje
    decrypted_message = cipher_suite.decrypt(message_bytes.encode())
    logging.info("Mensaje desencriptado")

    # Mostrar el mensaje desencriptado después de 2 segundos 
    window.after(2000, lambda: entrada_texto.insert(tk.END, decrypted_message.decode()))

window = tk.Tk()
window.title("AMAEME")

entrada_texto = tk.Text(window, height=5)
entrada_texto.pack(padx=10, pady=10)

boton_incluir = tk.Button(window, text="AMA - Asistente de Mensajería Anónima (Incluir)", command=incluir_mensaje)
boton_incluir.pack(fill=tk.X, padx=10, pady=5)

boton_extraer = tk.Button(window, text="EME - Extractor de Mensajería Encriptada (Extraer)", command=extraer_mensaje)
boton_extraer.pack(fill=tk.X, padx=10, pady=5)

window.mainloop()

#Como funciona??


[![Alt text](https://img.youtube.com/vi/XXPPE2gnC1Q/0.jpg)](https://www.youtube.com/watch?v=XXPPE2gnC1Q)



# AMAEME - Asistente de Mensajería Anónima y Extractor de Mensajería Encriptada

AMAEME es una herramienta de esteganografía que permite a los usuarios ocultar mensajes dentro de imágenes y luego recuperar esos mensajes. 
La herramienta utiliza técnicas de cifrado para asegurar que el mensaje sólo pueda ser leído por la persona que posea la clave de cifrado.

## Requisitos

- Python 3.8 o superior.
- Los paquetes de Python PIL, stepic, cryptography y tkinter deben estar instalados. Puedes instalarlos utilizando pip:

'pip install pillow stepic cryptography tkinter'


## Funciones

La herramienta tiene dos funciones principales:

- **Asistente de Mensajería Anónima (AMA)**: Permite al usuario seleccionar una imagen (JPEG, BMP o PNG) y escribir un mensaje. 
El mensaje se cifra y se oculta dentro de la imagen. La imagen resultante se guarda en el disco.

- **Extractor de Mensajería Encriptada (EME)**: Permite al usuario seleccionar una imagen que contiene un mensaje oculto. 
El mensaje se extrae, se descifra y se muestra al usuario.

## Uso

1. Ejecuta el script Python en tu terminal con el comando `python3 amaeme.py`.
2. Se abrirá una interfaz de usuario con una caja de texto y dos botones con la funcionalidades AMA y EME.
3. Para ocultar un mensaje, escribe el mensaje en la caja de texto y haz clic en el botón AMA. 
Se te pedirá que selecciones una imagen y luego que guardes la imagen resultante.
4. Para extraer un mensaje, haz clic en el botón EME. Se te pedirá que selecciones una imagen. 
Si la imagen contiene un mensaje oculto, se mostrará en la caja de texto.

## Nota

La clave de cifrado se guarda en un archivo .key en el mismo directorio y con el mismo nombre base que la imagen esteganografiada. 
Debes mantener este archivo .key seguro para poder descifrar el mensaje más tarde. Si la clave se pierde, el archivo no podrá descifrarse.

## Licencia

Este proyecto está licenciado bajo la GNU General Public License v3.0 - vea el archivo [LICENSE](LICENSE) para más detalles.


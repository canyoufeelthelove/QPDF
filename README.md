# 📝 Eliminador de Texto en PDF (PyMuPDF)

Este script permite **eliminar texto específico de archivos PDF** conservando el formato visual lo más posible. Utiliza la biblioteca [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) para buscar y cubrir instancias del texto con rectángulos blancos.

-------------------------------------------------------------------------------------------------------------

## 🚀 Características
✅ Busca texto exacto en archivos PDF.  
✅ Aplica redacción (cubriendo con rectángulo blanco) para eliminar el texto.  
✅ Guarda el archivo modificado con un sufijo "_limpio".  
✅ Interfaz de línea de comandos con selección interactiva de archivos PDF.  
✅ Permite procesar múltiples archivos o salir del programa.  

-------------------------------------------------------------------------------------------------------------

## 🛠 Requisitos
- **Python 3.7+**
- **PyMuPDF (fitz)**  
Instalar con:
```bash
pip install PyMuPDF
````

-------------------------------------------------------------------------------------------------------------

## 🏃‍♂️ Uso

1️⃣ Coloca el script en una carpeta con archivos PDF.
2️⃣ Ejecuta el script:

```bash
python eliminar_texto_pdf.py
```

3️⃣ Selecciona el archivo PDF deseado.
4️⃣ Ingresa el **texto exacto** que deseas eliminar.
5️⃣ Se generará un nuevo archivo PDF con el sufijo `_limpio`.

-------------------------------------------------------------------------------------------------------------

## ⚠️ Consideraciones

* La búsqueda de texto es **sensible a mayúsculas y minúsculas** y debe coincidir exactamente con lo que aparece en el PDF.
* El método cubre el texto con un rectángulo blanco; si el fondo del documento es de otro color, esto puede notarse.
* El formato puede verse ligeramente afectado dependiendo de la disposición original del PDF.

-------------------------------------------------------------------------------------------------------------

## 📂 Estructura

```
.
├── eliminar_texto_pdf.py   # Script principal
├── README.md               # (este archivo)
└── (coloca aquí tus archivos PDF)
```

-------------------------------------------------------------------------------------------------------------

## 🖋 Licencia

Este proyecto es de uso libre para fines educativos o personales. No se ofrece ninguna garantía sobre su efectividad en documentos críticos o confidenciales


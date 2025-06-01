import fitz  # PyMuPDF
import os
import sys

def eliminar_texto_conservando_formato(pdf_path, texto_a_eliminar):
    doc = fitz.open(pdf_path)
    paginas_afectadas = 0

    for pagina in doc:
        instancias = pagina.search_for(texto_a_eliminar)
        if instancias:
            paginas_afectadas += 1
            for rect in instancias:
                pagina.add_redact_annot(rect, fill=(1, 1, 1))  # blanco
            pagina.apply_redactions()

    if paginas_afectadas > 0:
        nombre_salida = os.path.splitext(pdf_path)[0] + "_limpio.pdf"
        doc.save(nombre_salida)
        print(f"\n✅ Guardado: {nombre_salida}")
    else:
        print("\n⚠️ Texto no encontrado en el documento.")

    doc.close()

def confirmar_salida():
    confirmacion = input("\n¿Deseas salir del programa? (s/n): ").strip().lower()
    if confirmacion == "s":
        print("Saliendo del programa.")
        sys.exit()  # Cambiado a sys.exit()
    else:
        print("Volviendo al menú...")

def main():
    try:
        while True:
            carpeta = os.getcwd()
            archivos_pdf = [f for f in os.listdir(carpeta) if f.lower().endswith(".pdf")]

            if not archivos_pdf:
                print("No se encontraron archivos PDF en la carpeta.")
                confirmar_salida()
                continue

            print("\n=== Selecciona un archivo PDF ===")
            for i, nombre in enumerate(archivos_pdf, start=1):
                print(f"{i}. {nombre}")
            print("0. Salir")

            try:
                opcion = int(input("\nIngresa el número del archivo: "))
                if opcion == 0:
                    confirmar_salida()
                    continue
                if not (1 <= opcion <= len(archivos_pdf)):
                    raise ValueError("Número fuera de rango.")
            except ValueError as e:
                print(f"Opción inválida: {e}")
                continue

            archivo_seleccionado = archivos_pdf[opcion - 1]
            ruta_pdf = os.path.join(carpeta, archivo_seleccionado)
            texto_a_eliminar = input("Texto exacto a eliminar del PDF: ").strip()
            eliminar_texto_conservando_formato(ruta_pdf, texto_a_eliminar)

            otra_accion = input("\n¿Deseas procesar otro archivo? (s/n): ").strip().lower()
            if otra_accion != "s":
                confirmar_salida()

    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        confirmar_salida()

if __name__ == "__main__":
    main()

# linea para compliar
# pyinstaller --onefile --console --icon=pdf.ico QPDF.py

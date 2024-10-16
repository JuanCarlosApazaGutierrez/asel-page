import os
from PIL import Image

def compress_images_in_folder(input_folder, output_folder, quality=70):
    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Recorre todos los archivos de la carpeta de entrada
    for filename in os.listdir(input_folder):
        # Verifica si el archivo es una imagen (puedes agregar más extensiones si es necesario)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            
            # Abre la imagen y la comprime
            image = Image.open(input_image_path)
            image.save(output_image_path, optimize=True, quality=quality)
            
            print(f'Imagen {filename} comprimida y guardada en {output_image_path}')

# Ejemplo de uso
input_folder = 'images'  # Carpeta de entrada con las imágenes
output_folder = 'reducida'  # Carpeta de salida para las imágenes comprimidas
compress_images_in_folder(input_folder, output_folder, quality=70)  # Ajusta la calidad si es necesario

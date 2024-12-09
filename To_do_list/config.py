# config.py
"""
    En este archivo, defino una función para calcular las coordenadas necesarias para
    centrar las ventanas en la pantalla.
"""
# config.py
def obtener_ruta_db():
    # Especifica la ruta completa donde quieres guardar la base de datos
    ruta_db = 'db/to_do_list.db'
    return ruta_db

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    
    x = int((pantalla_ancho / 2) - (ancho / 2))
    y = int((pantalla_alto / 2) - (alto / 2))
    
    return f'{ancho}x{alto}+{x}+{y}'
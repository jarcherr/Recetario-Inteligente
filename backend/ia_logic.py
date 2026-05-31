import os

def generar_receta_ia(ingredientes_usuario: str):
    # Ruta al archivo de recetas
    ruta_recetas = os.path.join("..", "data", "recetas_locales.txt")
    
    try:
        with open(ruta_recetas, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        # Lógica de búsqueda simple (Simulando RAG)
        # Dividimos el archivo por líneas para buscar
        recetas = contenido.split("\n")
        encontradas = [r for r in recetas if ingredientes_usuario.lower() in r.lower()]

        if encontradas:
            return {
                "receta": encontradas[0],
                "info": "Encontrada en tu base de datos local",
                "status": "success"
            }
        else:
            return {
                "receta": "No encontré nada exacto, pero te sugiero un Omelet.",
                "info": "Sugerencia general de la IA",
                "status": "not_found"
            }
    except FileNotFoundError:
        return {"error": "No se encontró la base de datos de recetas."}
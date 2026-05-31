import os

def generar_receta_ia(ingredientes_usuario: str):
    try:
        base_path = os.path.dirname(__file__)
        ruta_txt = os.path.join(base_path, "..", "data", "recetas_locales.txt")
        
        with open(ruta_txt, "r", encoding="utf-8") as f:
            # Dividimos el archivo en recetas individuales usando '---' como separador
            biblioteca_recetas = f.read().split("---") 

        busqueda = ingredientes_usuario.lower().strip()
        receta_seleccionada = None
        
        # Buscamos la receta que contenga el ingrediente
        for receta in biblioteca_recetas:
            if busqueda in receta.lower():
                receta_seleccionada = receta.strip()
                break # Detenemos la búsqueda al encontrar la primera coincidencia
        
        if receta_seleccionada:
            # Solo enviamos la receta encontrada, no todo el archivo
            mensaje = receta_seleccionada
        else:
            mensaje = f"No encontré una receta específica con '{ingredientes_usuario}'. Intenta con ingredientes base como 'huevo', 'fresa' o 'avena'."

        return {
            "receta": mensaje,
            "info": "Motor RAG Local (Modo Compatibilidad Python 3.14)",
            "status": "success"
        }

    except Exception as e:
        return {"receta": f"Error: {str(e)}", "status": "error"}
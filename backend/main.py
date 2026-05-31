from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # IMPORTANTE
from ia_logic import generar_receta_ia

app = FastAPI()

# --- Configuración de CORS (Copia esto tal cual) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Esto permite que cualquier origen (como tu frontend) se conecte
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------------------------

@app.get("/")
def read_root():
    return {"message": "Servidor de Recetas IA activo"}

@app.get("/buscar")
def buscar_receta(ingredientes: str):
    resultado = generar_receta_ia(ingredientes)
    return resultado
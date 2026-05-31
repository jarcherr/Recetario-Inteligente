from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡El servidor del Recetario está funcionando!"}

@app.get("/status")
def get_status():
    return {"status": "IA lista para cocinar", "version": "0.1"}
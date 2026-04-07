from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API de soma funcionando!"}

@app.get("/somar")
def somar(a: float, b: float):
    resultado = a + b
    return {
        "numero1": a,
        "numero2": b,
        "resultado": resultado
    }

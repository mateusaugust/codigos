from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API rodando no Render 🚀"}

@app.get("/soma")
def soma(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "resultado": a + b
    }

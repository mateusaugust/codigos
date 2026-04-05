from fastapi import FastAPI

app = FastAPI()

@app.get("/numeros/")
def obter_numeros(inicio: int, fim: int):
    if inicio > fim:
        inicio, fim = fim, inicio
    
    numeros = list(range(inicio + 1, fim))
    
    return {
        "inicio": inicio,
        "fim": fim,
        "numeros_entre": numeros
    }
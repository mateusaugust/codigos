from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(
    title="API Soma e Divide",
    description="Recebe dois valores via URL, soma e divide por 10.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "mensagem": "API funcionando!",
        "uso": "/calcular?a=20&b=30",
        "descricao": "Soma dois valores e divide por 10"
    }


@app.get("/calcular")
def calcular(
    a: float = Query(..., description="Primeiro valor"),
    b: float = Query(..., description="Segundo valor")
):
    soma = a + b
    resultado = soma / 10

    return JSONResponse(content={
        "a": a,
        "b": b,
        "soma": soma,
        "resultado": resultado,
        "operacao": f"({a} + {b}) / 10 = {resultado}"
    })

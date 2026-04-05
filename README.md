# API Soma e Divide

API simples que recebe dois valores via URL, soma e divide o resultado por 10.

## Endpoints

### `GET /`
Retorna informações sobre a API.

### `GET /calcular?a=VALUE&b=VALUE`
Soma `a` e `b` e divide por 10.

**Exemplo:**
```
GET /calcular?a=20&b=30
```

**Resposta:**
```json
{
  "a": 20,
  "b": 30,
  "soma": 50,
  "resultado": 5.0,
  "operacao": "(20 + 30) / 10 = 5.0"
}
```

---

## Como rodar localmente

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse: `http://localhost:8000`

Documentação automática: `http://localhost:8000/docs`

---

## Deploy no Render

1. Suba este projeto para um repositório GitHub
2. Acesse [render.com](https://render.com) e crie uma conta
3. Clique em **New > Web Service**
4. Conecte seu repositório GitHub
5. Preencha as configurações:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Clique em **Deploy**

Pronto! Sua API estará disponível na URL gerada pelo Render.

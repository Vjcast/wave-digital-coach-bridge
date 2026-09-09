# Wave Digital Coach Bridge

API puente segura para conectar un GPT personalizado con datos públicos de Bybit.

## Qué hace

- Lee velas públicas de Bybit mediante `/v5/market/kline`.
- Calcula:
  - SMA 3
  - SMA 9
  - SMA 20
  - DMI / ADX 14
  - Volume MA20
- Devuelve una lectura tipo Wave Digital:
  - estructura SMA
  - dominio +DI / -DI
  - ADX
  - compresión de medias
  - volumen relativo
  - score LONG / SHORT
  - acción educativa sugerida

## Qué NO hace

- No opera.
- No crea órdenes.
- No lee saldos.
- No necesita API key de Bybit.
- No toca fondos.

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abrir:

```text
http://127.0.0.1:8000/market-state?symbol=BTCUSDT&interval=1&category=linear&limit=200
```

## Desplegar en Render

1. Sube esta carpeta a GitHub.
2. En Render, crea un Web Service desde el repo.
3. Usa:

```bash
Build command: pip install -r requirements.txt
Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

4. Copia tu URL pública, por ejemplo:

```text
https://wave-digital-coach-bridge.onrender.com
```

5. Edita `openapi.yaml` y reemplaza:

```text
https://TU-DOMINIO-RENDER.onrender.com
```

por tu URL real.

## Crear el GPT

1. En ChatGPT, entra a Explorar GPTs / Crear.
2. Nombre sugerido: `Wave Digital Coach — BTC/ETH 1M`.
3. Pega el contenido de `gpt_instructions.md` en Instructions.
4. En Actions, crea una nueva acción.
5. Pega el contenido de `openapi.yaml`.
6. Autenticación: `None`, porque esta primera versión solo usa datos públicos.
7. Prueba la acción con:

```text
getMarketState symbol=BTCUSDT interval=1 category=linear limit=200
```

## Nota para Victor

Esta versión es de entrenamiento. Sirve para leer mercado y practicar disciplina. La versión con saldo, posiciones u órdenes requeriría API privada read-only y otra capa de seguridad.

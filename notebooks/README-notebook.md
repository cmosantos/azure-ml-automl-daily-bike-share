# Notebook para Consumo do Modelo – Azure ML

Este diretório é destinado aos notebooks utilizados para testar e consumir o modelo publicado no Azure Machine Learning.

### Exemplo de notebook sugerido: `consume_model.ipynb`

O código abaixo pode ser usado dentro do notebook para enviar dados ao endpoint do modelo:

```python
import json
import requests

endpoint = "<YOUR_ENDPOINT_URL>"
api_key = "<YOUR_API_KEY>"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
  "Inputs": {
    "data": [{
        "day": 1,
        "mnth": 1,
        "year": 2022,
        "season": 2,
        "holiday": 0,
        "weekday": 1,
        "workingday": 1,
        "weathersit": 2,
        "temp": 0.3,
        "atemp": 0.3,
        "hum": 0.3,
        "windspeed": 0.3
    }]
  }
}

response = requests.post(endpoint, headers=headers, json=payload)
response.json()
```

Use este diretório para criar seus notebooks de teste e validação do modelo.


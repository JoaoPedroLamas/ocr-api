## OCR API

### Parameters

- `urlImage` (required): URL of the image to be processed
- `proxy` (optional): Proxy to be used for the request

### Response

- `json`: JSON object containing the result of the OCR process

### Example

```python
import httpx

urlImage = 'https://pbs.twimg.com/media/GxRTiCrWsAA3Egv?format=jpg&name=medium'
proxy = 'http://127.0.0.1:8080'
response = httpx.get(urlImage, proxies=proxy)
print(response.json())
```

### Response

```json
{
    "ParsedResults": [
        {
            "ParsedText": "Text extracted from the image"
        }
    ]
}
```

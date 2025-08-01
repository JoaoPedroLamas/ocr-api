import httpx

def ocr(urlImage, proxy=None):
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6',
        'apikey': 'donotstealthiskey_ip1',
        'cache-control': 'no-cache',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryq0d0jWM6HcEdr5Hy',
        'dnt': '1',
        'origin': 'https://ocr.space',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://ocr.space/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }

    files = {
        'url': (None, urlImage),
        'language': (None, 'auto'),
        'isOverlayRequired': (None, 'true'),
        'FileType': (None, '.Auto'),
        'IsCreateSearchablePDF': (None, 'false'),
        'isSearchablePdfHideTextLayer': (None, 'true'),
        'detectOrientation': (None, 'false'),
        'isTable': (None, 'false'),
        'scale': (None, 'true'),
        'OCREngine': (None, '5'),
        'detectCheckbox': (None, 'false'),
        'checkboxTemplate': (None, '0'),
    }

    response = httpx.post('https://api8.ocr.space/parse/image', headers=headers, files=files, proxy=proxy)
    if response.status_code != 200:
        return None
    return response.json()


urlImage = 'https://pbs.twimg.com/media/GxRTiCrWsAA3Egv?format=jpg&name=medium'

data = ocr(urlImage)
#print(data['ParsedResults'][0]['ParsedText'])
print(data)
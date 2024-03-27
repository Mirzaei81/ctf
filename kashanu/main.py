import requests
cookies = {
    'h1': 'dW5zZXJpYWxpemU%3D',
    'h2': 'ZmlsZS56aXA%3D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'h1=dW5zZXJpYWxpemU%3D; h2=ZmlsZS56aXA%3D',
    'Pragma': 'no-cache',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

for i in range(1001):
    params = {
        'id': f'{i}',
    }
    response = requests.get('http://82.115.18.192:5003/', params=params, cookies=cookies, headers=headers, verify=False)
    print(response.url)
    print(response.text)

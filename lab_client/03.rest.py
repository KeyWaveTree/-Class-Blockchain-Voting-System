import requests
import json

#post 요청은 컨텐츠 타입을 불러줘야할 명시를 적어줘야 한다.
headers={'Content-Type': 'application/json'}

data={
    'id': '0',
    'vote': 'A1',
}
res= requests.post('http://127.0.0.1:5000/open', data=json.dumps(data), headers=headers)
print(res.text)
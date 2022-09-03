import requests
import json

#post 요청은 컨텐츠 타입을 불러줘야할 명시를 적어줘야 한다.
headers={'Content-Type': 'application/json'}

data={
    'question':'Q1',
    'options': ['A1', 'A2', 'A3']
}
print(data)
print(json.dumps(data))
print(type(data))
print(type(json.dumps(data)))
res= requests.post('http://127.0.0.1:5000/open', data=json.dumps(data), headers=headers)
print(res.text)
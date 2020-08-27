import requests
result = requests.get("http://52.90.199.190:5000/?msg=HelloWorld!")
print(result.json())
result = requests.get("http://52.90.199.190:5000/",
params = { 'msg': 'Hello from params' })
print(result.json())
result = requests.post("http://52.90.199.190:5000/",
json = { 'msg': 'Hello from data' })
print(result.json())

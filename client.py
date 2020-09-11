import requests

r = requests.get('http://localhost:8000/file.html')
print(r.text)
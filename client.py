import requests

r = requests.get('http://localhost:8000/file.html')
print('Reply status code %s\nContent:\n%s\n\n' % (r.status_code, r.text))

r = requests.get('http://localhost:8000/non_existent_file.html')
print('Reply status code %s\nContent:\n%s\n\n' % (r.status_code, r.text))

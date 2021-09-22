import requests
import json

r = requests.get('http://localhost:8000/file.html')
print('Reply status code %s\nContent:\n%s\n\n' % (r.status_code, r.text))

r = requests.get('http://localhost:8000/non_existent_file.html')
print('Reply status code %s\nContent:\n%s\n\n' % (r.status_code, r.text))

throw = {'throw': 'paper'}
r = requests.post('http://localhost:8000/game_7/play_3/player_2', json=json.dumps(throw))
print('Reply status code %s\nContent:\n%s\n\n' % (r.status_code, r.text))
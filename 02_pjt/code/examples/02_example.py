# requests 사용 예시 2

import requests


URL = 'https://api.agify.io'
BASE_URL='https://api.themoviedb.org/3/'
path=''
'''
pr = {
    'name': 'michael',
    'country_id': 'KR',
}
'''
pr = {
    'api_key' : '545308fe254ef103d9a0e7a451bca4b5'
}
response = requests.get(URL, params=pr).json()
print(response)

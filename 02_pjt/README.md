# Problem_a

* requests 모듈 사용법을 익혔다.

* 2가지 방법

* ```
  BASE_URL='https://api.themoviedb.org/3/'
  path='movie/popular?'
  pr={
      'api_key' : '545308fe254ef103d9a0e7a451bca4b5',
      'language' : 'en-US',
  }
  response = requests.get(BASE_URL+path,params=pr).json()
  ```

* ```
  URL = 'https://dog.ceo/api/breeds/image/random'
  response = requests.get(URL).json()
  ```

# 

# Problem_b



# Problem_c

- 수업중에 배웠던 sorted(?,key=?)와 lambda를 사용할 수 있었다. 



# Problem_d

- String.format()을 사용하여 문자열을 처리했다.



# Problem_e

- requests 모듈을 사용하여 영화 검색 사이트 api에 http 요청 하는 것을 공부할 수 있었다.

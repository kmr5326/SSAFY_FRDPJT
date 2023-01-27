import requests

#545308fe254ef103d9a0e7a451bca4b5 api key

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    #URL = 'https://api.themoviedb.org/3/movie/popular?api_key=545308fe254ef103d9a0e7a451bca4b5&language=en-US&page=1'
    BASE_URL='https://api.themoviedb.org/3/'
    path='movie/popular?'
    pr={
        'api_key' : '545308fe254ef103d9a0e7a451bca4b5',
        'language' : 'en-US',
    }
    response = requests.get(BASE_URL+path,params=pr).json()
    return len(response.get('results'))


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20


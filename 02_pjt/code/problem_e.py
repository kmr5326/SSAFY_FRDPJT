import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    BASE_URL='https://api.themoviedb.org/3/'
    path='search/movie?'
    pr={
        'api_key' : '545308fe254ef103d9a0e7a451bca4b5',
        'language' : 'en-US',
        'query' : title
    }
    response = requests.get(BASE_URL+path,params=pr).json()
    result = response.get('results')
    
    if len(result)>0:
        BASE_URL='https://api.themoviedb.org/3/'
        path='movie/{0}/credits?'.format(result[0].get('id'))
        pr={
            'api_key' : '545308fe254ef103d9a0e7a451bca4b5',
            'language' : 'en-US',
        }
        response = requests.get(BASE_URL+path,params=pr).json()
        casts = response.get('cast')
        cast_list=[]
        for cast in casts:
            if cast.get('cast_id')<10:
                cast_list.append(cast.get('name'))
        crews = response.get('crew')
        crew_list=[]
        for crew in crews:
            if crew.get('department')=='Directing':
                crew_list.append(crew.get('name'))
        cast_crew_list={
            'cast' : cast_list,
            'crew' : crew_list
        }
        return cast_crew_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    lst=[]
    for movie in movies:
        _id=movie.get('id')
        m = open(f'data/movies/{_id}.json', encoding='utf-8')
        movie_detail=json.load(m)
        if movie_detail.get('release_date')[5:7]=='12':
            lst.append(movie_detail.get('title'))
    return lst

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

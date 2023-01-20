import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    max=0
    title=''
    for movie in movies:
        _id=movie.get('id')
        m = open(f'data/movies/{_id}.json', encoding='utf-8')
        movie_detail=json.load(m)
        if movie_detail.get('revenue')>max:
            max=movie_detail.get('revenue')
            title=movie_detail.get('title')
    return title
    # movie = open('sample.json', encoding='utf-8')
    # movie_detail = json.load(movie)
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

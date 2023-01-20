import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    import problem_a as A
    new_dict=A.movie_info(movie)
    names=[]
    for ids in new_dict['genre_ids']:
        for genre in genres:
            if genre.get('id')==ids:
                names.append(genre.get('name'))
    new_dict['genre_names']=names
    del new_dict['genre_ids']
    return new_dict

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

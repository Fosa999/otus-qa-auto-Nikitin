from hw4.src.base_api import BaseApi


class JsonplaceApi(BaseApi):

    BASE_URL_JSONPLACE = 'https://jsonplaceholder.typicode.com'

    posts = '/posts'
    posts_form = '/posts/{}'
    comments = '/comments'
    comments_form = '/comments{}'
    users = '/users'
    def __init__(self):
        super().__init__(JsonplaceApi.BASE_URL_JSONPLACE)

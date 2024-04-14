from hw4.src.base_api import BaseApi


class DogApi(BaseApi):

    BASE_URL_DOG = 'https://dog.ceo'

    Breed_list_all = '/api/breeds/list/all'
    By_breed = '/api/breed/hound/images'
    by_sub_breed = '/api/breed/{}/list'
    Random_one = '/api/breed/hound/images/random/{}'
    Breed_list_one = "/api/breed/{}/images/random"

    def __init__(self):
        super().__init__(DogApi.BASE_URL_DOG)

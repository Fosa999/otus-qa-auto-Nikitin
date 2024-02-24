import pytest
from hw4.src.dog_api import DogApi
# base_url = "https://dog.ceo/api"  # Замените на базовый URL вашего API


@pytest.fixture
def dog_api():
    return DogApi()


class TestDog:
    """ Получение списка всех пород"""
    def test_get_all_breeds(self, dog_api):
        response = dog_api.get(DogApi.Breed_list_all)
        assert response.status_code == 200  # Проверяем, что статус-код ответа - 200
        data = response.json()
        assert "message" in data
        assert isinstance(data["message"], dict)
        assert data["status"] == 'success'

    """Возврат подпород собак (если есть)"""
    @pytest.mark.parametrize("sub_breed", ["australian", "buhund", "bulldog", "bullterrier"])
    def test_get_sub_breed(self, dog_api, sub_breed):
        response = dog_api.get(DogApi.by_sub_breed.format(sub_breed))
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert isinstance(data["message"],list)
        assert data["status"] == "success"

    """Массив всех картинок по породам"""
    def test_get_by_breed(self, dog_api):
        response = dog_api.get(DogApi.By_breed)
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert isinstance(data["message"], list)
        assert data["status"] == 'success'

    '''Количество отображения рандомных картинок'''
    @pytest.mark.parametrize("count", [1, 2, 3])
    def test_random_count_images(self, dog_api, count):
        response = dog_api.get(DogApi.Random_one.format(count))
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert isinstance(data["message"], list)
        assert data["status"] == 'success'

    '''Рандомная картинка по породе'''
    @pytest.mark.parametrize('breed', ['affenpinscher', 'african', 'pug'])
    def test_breed_list_one(self, dog_api, breed):
        response = dog_api.get(DogApi.Breed_list_one.format(breed))
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert isinstance(data["message"], str)
        assert data["status"] == 'success'

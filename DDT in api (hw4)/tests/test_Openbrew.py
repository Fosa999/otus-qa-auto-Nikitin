import pytest
from hw4.src.openbrew_api import OpenBrewApi


@pytest.fixture
def brew_api():
    return OpenBrewApi()


class TestOpenBrew:
    """Получение данных по одной пивоварне"""

    @pytest.mark.parametrize("id_brew", ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
                                         "5128df48-79fc-4f0f-8b52-d06be54d0cec",
                                         "9c5a66c8-cc13-416f-a5d9-0a769c87d318",
                                         "34e8c68b-6146-453f-a4b9-1f6cd99a5ada"])
    def test_single_brewery(self, brew_api, id_brew):
        response = brew_api.get(OpenBrewApi.breweries_list.format(id_brew))
        assert response.status_code == 200
        data = response.json()
        assert "id" in data and "name" in data and "city" in data and "country" in data
        assert (isinstance(data["id"], str) and isinstance(data["name"], str) and isinstance(data["city"], str)
                and isinstance(data["country"], str))
        assert 'Content-Type' in response.headers

    '''Получение всех пивоварен'''

    def test_list_brewery(self, brew_api):
        response = brew_api.get(OpenBrewApi.breweries_list.format(""))
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 50
        assert 'Content-Type' in response.headers

    '''Получение 2х пивоварен по id'''

    @pytest.mark.parametrize('id_brews',
                             [["701239cb-5319-4d2e-92c1-129ab0b3b440",
                               "06e9fffb-e820-45c9-b107-b52b51013e8f"],
                              ["1630747e-8c36-4a34-9531-02d6b5ac2a28",
                               "53efe9e9-dbb3-4c98-ab77-61515abef2a9"]])
    def test_by_ids(self, brew_api, id_brews):
        """Здесь я использую ','.join(id_brews) чтобы объединить все ID в строку с разделителем ','.
        Таким образом, в параметре by_ids будет передан список ID в формате, который ожидает API."""
        response = brew_api.get(OpenBrewApi.breweries_list_param, params={'by_ids': ','.join(id_brews)})
        assert response.status_code == 200
        data = response.json()
        for ids in data:
            assert 'id' in ids and 'id' is not None
            assert 'name' in ids and 'name' is not None
            assert 'country' in ids and 'country' is not None
        assert len(data) == len(id_brews)
        assert 'Content-Type' in response.headers

    def test_by_random(self, brew_api):
        response = brew_api.get(OpenBrewApi.breweries_list.format("random"))
        assert response.status_code == 200
        data = response.json()
        for ids in data:
            assert 'id' in ids and 'id' is not None
            assert 'name' in ids and 'name' is not None
            assert 'country' in ids and 'country' is not None
        assert 'Content-Type' in response.headers

    @pytest.mark.parametrize(('country', 'per_page'), [('United States', 1),
                                                       ('United States', 3),
                                                       ('South Korea', 1)])
    def test_by_city(self, brew_api, country, per_page):
        response = brew_api.get(OpenBrewApi.breweries_list_param, params={'by_country': country, "per_page": per_page})
        assert response.status_code == 200
        data = response.json()
        for ids in data:
            assert 'id' in ids and 'id' is not None
            assert 'name' in ids and 'name' is not None
            assert 'country' in ids and 'country' is not None
        assert len(data) == per_page
        assert 'Content-Type' in response.headers

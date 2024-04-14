import pytest
from hw4.src.jsonplace_api import JsonplaceApi


# base_url = "https://dog.ceo/api"  # Замените на базовый URL вашего API


@pytest.fixture
def place_api():
    return JsonplaceApi()


class TestJsonPlace:
    """Получаем список постов"""

    def test_list_posts(self, place_api):
        response = place_api.get(JsonplaceApi.posts)
        assert response.status_code == 200
        data = response.json()
        for field in data:
            assert "userId" in field
            assert "title" in field
            assert "body" in field
            assert "id" in field
        assert 'Content-Type' in response.headers

    '''Ищем посты по id'''

    @pytest.mark.parametrize("ids", [2, 3, 4, 5])
    def test_id_posts(self, place_api, ids):
        response = place_api.get(JsonplaceApi.posts_form.format(ids))
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == ids
        assert "userId" in data is not None
        assert "title" in data is not None
        assert "body" in data is not None
        assert len(data) == 4

    def test_get_comments(self, place_api):
        response = place_api.get(JsonplaceApi.comments)
        assert response.status_code == 200
        data = response.json()
        for field in data:
            assert "postId" in field
            assert "id" in field
            assert "name" in field
            assert "email" in field
            assert "body" in field
        assert 'Content-Type' in response.headers

    @pytest.mark.parametrize("id_post", [1, 2, 3, 4, 5])
    def test_get_comments_for_posts(self, place_api, id_post):
        response = place_api.get(JsonplaceApi.posts_form.format(id_post, '/comments'))
        assert response.status_code == 200
        data = response.json()
        for field in data:
            assert "postId" in field
            assert "id" in field
            assert "name" in field
            assert "email" in field
            assert "body" in field
        assert 'Content-Type' in response.headers

    def test_get_users(self, place_api):
        response = place_api.get(JsonplaceApi.users)
        assert response.status_code == 200
        data = response.json()
        for field in data:
            assert "id" in field
            assert "name" in field
            assert "email" in field
        assert 'Content-Type' in response.headers

    @pytest.mark.parametrize(
        'data',
        ([
            {
                'title': 'test_title',
                'body': 'test_body',
                'userId': 10
            }
        ])
    )
    def test_create_post(self, place_api, data):
        response = place_api.post(JsonplaceApi.posts, data=data)
        assert response.status_code == 201
        post = response.json()
        assert post, 'Post is empty'
        assert post['title'] == data['title']
        assert post['body'] == data['body']
        assert post['userId'] == str(data['userId'])

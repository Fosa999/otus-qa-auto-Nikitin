import requests


def test_status_code(request):
    url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")

    response = requests.get(url)
    assert response.status_code == status_code

import requests


class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        return requests.get(url, params)

    def put(self, endpoint):
        url = self.base_url + endpoint
        return requests.put(url)

    def post(self, endpoint, data=None):
        url = self.base_url + endpoint
        return requests.post(url, data)

    def delete(self, endpoint):
        url = self.base_url + endpoint
        return requests.delete(url)

    # log part
    print()
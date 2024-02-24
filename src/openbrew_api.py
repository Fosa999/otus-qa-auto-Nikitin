from hw4.src.base_api import BaseApi


class OpenBrewApi(BaseApi):

    BASE_URL_OPENBREW = 'https://api.openbrewerydb.org'

    breweries_list = '/v1/breweries/{}'
    breweries_list_param = '/v1/breweries'

    def __init__(self):
        super().__init__(OpenBrewApi.BASE_URL_OPENBREW)

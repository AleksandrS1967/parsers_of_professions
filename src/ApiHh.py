from src.AbstractApi import AbstractApi
import json
import requests


class ApiHh(AbstractApi):
    def get_vacancy(self, search_query: str):
        keys = {'text': f'NAME: {search_query.lower()}', 'area': 113, 'per_page': 100}
        vacancy = requests.get('https://api.hh.ru/vacancies', keys)
        return json.loads(vacancy.text)['items']
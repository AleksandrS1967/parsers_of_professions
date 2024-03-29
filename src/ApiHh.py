from start_pack.AbstractApi import AbstractApi
import json
import requests


class ApiHh(AbstractApi):
    """класс для работы с API"""
    def get_vacancy(self, search_query: str, link_hh):
        """Получение вакансий по API используя запрос пользователя"""
        keys = {'text': f'NAME:{search_query}', 'area': 113, 'per_page': 100}
        vacancy = requests.get(link_hh, keys)
        try:
            return json.loads(vacancy.text)['items']
        except KeyError:
            print(f'Увы, но запрос ({search_query}) не прошел... Возможно неполадки на сервере(')
            return None

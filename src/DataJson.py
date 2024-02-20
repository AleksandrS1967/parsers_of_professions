from start_pack.AbstractData import AbstractData
import json


class DataJson(AbstractData):
    """класс для работы с данными"""
    def get_data(self, vacancy_path):
        """Получение данных"""
        with open(vacancy_path, encoding='utf-8') as f:
            return json.load(f)

    def add_data(self, vacancy, vacancy_path):
        """Добавление данных"""
        with open(vacancy_path, 'w', encoding='utf-8') as f:
            json.dump(vacancy, f, ensure_ascii=False)

    def delete_data(self, vacancy_path):
        """Удаление данных"""
        with open(vacancy_path, 'w', encoding='utf-8') as f:
            v = ''
            json.dump(v, f, ensure_ascii=False)


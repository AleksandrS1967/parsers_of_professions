from abc import ABC, abstractmethod


class AbstractData(ABC):
    """Абстрактный класс для работы с данными"""
    @abstractmethod
    def get_data(self, vacancy_path):
        """Получение данных"""
        pass

    @abstractmethod
    def add_data(self, vacancy, vacancy_path):
        """Добавление данных"""
        pass

    @abstractmethod
    def delete_data(self, vacancy_path):
        """Удаление данных"""
        pass

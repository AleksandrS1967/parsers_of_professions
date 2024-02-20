from abc import ABC, abstractmethod


class AbstractApi(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_vacancy(self, search_query, link):
        """Получение вакансий по API используя запрос пользователя"""
        pass







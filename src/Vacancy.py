from heapq import nlargest


class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, vacancy: dict = None):
        try:
            self.__vacancy = vacancy
            self.name_vacancy = vacancy['name']
            self.link_vacancy = vacancy['alternate_url']
        except TypeError:
            self.__vacancy = None
            self.name_vacancy = None
            self.link_vacancy = None

    def __str__(self):
        return (f'Имя: {self.name_vacancy}\n'
                f'Зарплата: {self.salary_vacancy}\n'
                f'Ссылка: {self.link_vacancy}\n'
                f'Описание: {self.description}\n')

    @staticmethod
    def get_top_n(query_top_n, start_pack):
        """Получаем top_n и создаём список экземпляров каждой вакансии"""
        vacancy = start_pack.data_json.get_data(start_pack.vacancy_path)
        list_vacancy = []
        for i in vacancy:
            if i['salary']:
                list_vacancy.append(Vacancy(i))
        res = nlargest(query_top_n, list_vacancy, key=lambda x: x.salary_vacancy)
        return res, list_vacancy

    @staticmethod
    def get_filter_words(filter_words: list, list_vacancy: list):
        """Фильтрует вакансии по описанию используя ключевые слова введенные пользователем"""
        filter_list = []
        for i in list_vacancy:
            for i_ in filter_words:
                if i_.lower() in i.description.lower():
                    filter_list.append(i)
        return filter_list

    @property
    def salary_vacancy(self):
        if self.__vacancy['salary']['from']:
            salary = self.__vacancy['salary']['from']
            return salary
        else:
            salary = self.__vacancy['salary']['to']
            return salary

    @property
    def description(self):
        if self.__vacancy['snippet']['requirement']:
            res = self.__vacancy['snippet']['requirement']
        else:
            res = ''
        if self.__vacancy['snippet']['responsibility']:
            res_ = self.__vacancy['snippet']['responsibility']
        else:
            res_ = ''
        return res + '\n' + res_




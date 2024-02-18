class Vacancy:
    """"""
    def __init__(self, vacancy: dict):
        self.__vacancy = vacancy
        self.name_vacancy = vacancy['name']
        self.link_vacancy = vacancy['alternate_url']

    def __str__(self):
        return (f'Имя: {self.name_vacancy}\n'
                f'Зарплата: {self.salary_vacancy}\n'
                f'Ссылка: {self.link_vacancy}')

    @property
    def salary_vacancy(self):
        if self.__vacancy['salary']['from']:
            salary = self.__vacancy['salary']['from']
            return salary
        else:
            salary = self.__vacancy['salary']['to']
            return salary


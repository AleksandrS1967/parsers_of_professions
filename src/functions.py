from heapq import nlargest
from src.Vacancy import Vacancy


def get_top_n(query_top_n, start_pack):
    vacancy = start_pack.data_json.get_data(start_pack.vacancy_path)
    list_vacancy = []
    for i in vacancy:
        if i['salary']:
            list_vacancy.append(Vacancy(i))
    res = nlargest(query_top_n, list_vacancy, key=lambda x: x.salary_vacancy)
    return res, list_vacancy


def get_filter_words(filter_words: list, list_vacancy: list):
    filter_list = []
    for i in list_vacancy:
        for i_ in filter_words:
            if i_.lower() in i.description.lower():
                filter_list.append(i)
    return filter_list




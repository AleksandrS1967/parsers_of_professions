

def app_operation(start_pack):
    search_query = input("Введите название вакансии для поиска: ")
    vacancy = start_pack.api_hh.get_vacancy(search_query)
    start_pack.data_json.add_data(vacancy, start_pack.vacancy_path)

    # query_top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # top_n, list_vacancy = start_pack.get_top_n(query_top_n, start_pack)





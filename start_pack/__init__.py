import pathlib #посмотреть что это
from start_pack.app_operation import app_operation
from src.ApiHh import ApiHh
from src.DataJson import DataJson
from src.Vacancy import Vacancy

project_path = pathlib.Path(__file__).parent.parent
vacancy_path = pathlib.Path(project_path, 'src', 'vacancy.json')
vacancy_instance = Vacancy()
link_hh = 'https://api.hh.ru/vacancies'

api_hh = ApiHh()
data_json = DataJson()



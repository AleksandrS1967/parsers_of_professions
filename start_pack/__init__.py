import pathlib #посмотреть что это
from start_pack.app_operation import app_operation
from src.ApiHh import ApiHh
from src.DataJson import DataJson
from src.functions import get_top_n

project_path = pathlib.Path(__file__).parent.parent
vacancy_path = pathlib.Path(project_path, 'src', 'vacancy.json')

api_hh = ApiHh()
data_json = DataJson()



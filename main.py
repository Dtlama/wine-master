import os
import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_ending(num):
    if num < 21 and num > 4:
        return 'лет'
    num = num % 10
    if num == 1:
        return 'год'
    elif num > 1 and num < 5:
        return 'года'
    return 'лет'


if __name__ == '__main__':
    foundation_year = 1920

    wines_file = pandas.read_excel(
        os.getenv('FILE_PATH', 'wine.xlsx'),
        sheet_name='Лист1',
        usecols=[
            'Категория',
            'Название',
            'Сорт',
            'Цена',
            'Картинка',
            'Акция'
        ],
        na_values=['nan'],
        keep_default_na=False
    )
    excel_data_df = wines_file.to_dict(orient='records')

    wines = collections.defaultdict(list)
    for wine in excel_data_df:
        wines[wine["Категория"]].append(wine)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    current_year = datetime.datetime.now().year
    winery_age = current_year - foundation_year

    ending_date = get_ending(winery_age)

    rendered_page = template.render(
        winery_age=winery_age,
        wines=wines,
        date_ending=ending_date
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

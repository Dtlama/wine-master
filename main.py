import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def ending(num, first, second, third):
    if num < 21 and num > 4:
        return third
    num = num % 10
    if num == 1:
        return first
    elif num > 1 and num < 5:
        return second
    return third


if __name__ == '__main__':
    foundation_year = 1920

    dicts = pandas.read_excel(
        'wine3.xlsx',
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
    excel_data_df = dicts.to_dict(orient='records')

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

    ending_date = ending(winery_age, "год", "года", "лет")

    rendered_page = template.render(
        winery_age=winery_age,
        wines=wines,
        date_ending=ending_date
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

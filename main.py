import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape

if __name__ == '__main__':

    dicts = pandas.read_excel('wine3.xlsx', sheet_name='Лист1',
                              usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'], na_values=['nan'],
                              keep_default_na=False)
    excel_data_df = dicts.to_dict(orient='records')

    wines = collections.defaultdict(list)
    for wine in excel_data_df:
        wines[wine["Категория"]].append(wine)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    event_1 = datetime.datetime.now().year
    year = event_1 - 1920

    rendered_page = template.render(
        today_year=year,
        wines=wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

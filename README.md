# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как установить

Пример файла с данными для сайта wine.xlsx уже находится в репозитории.
Можете заполнить этот файл своими данными.

[Python3](https://www.python.org/downloads/) должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```

pip install -r requirements.txt
```

## Запуск и использование

- Скачайте код
- Запустите сайт командой
```

python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
Если хотите указать свой путь или имя файла с данными для сайта, задайте переменную окружения `FILE_PATH`
В виде `FILE_PATH=ваш путь до файла`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

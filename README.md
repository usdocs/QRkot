# QRkot_spreadseets
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&&logoColor=ffffff&color=5fe620)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=5fe620)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=5fe620)](https://alembic.sqlalchemy.org/en/latest/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?style=flat&logo=Uvicorn&logoColor=ffffff&color=5fe620)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=5fe620)](https://docs.pydantic.dev/latest/)
[![FastAPI_Users](https://img.shields.io/badge/-FastAPI_Users-464646?style=flat&logo=FastAPI_Users&logoColor=ffffff&color=5fe620)](https://fastapi-users.github.io/fastapi-users/10.0/)
[![aiogoogle](https://img.shields.io/badge/-aiogoogle-464646?style=flat&logo=aiogoogle&logoColor=ffffff&color=5fe620)](https://aiogoogle.readthedocs.io/en/latest/)



## приложение для Благотворительного фонда поддержки котиков QRKot с функцией выгрузки отчета о закрытых проектах
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

Добавлена возможность для суперюзера формирования отчёта в гугл-таблице. В таблицу выгружаются закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

## Технологии проекта
* Python — высокоуровневый язык программирования.
* FastAPI — веб-фреймворк для создания API, написанный на Python. FastAPI активно использует декораторы, аннотации типов и интроспекцию кода, что позволяет уменьшить количество шаблонного кода в веб-приложении.
* SQLAlchemy — Программная библиотека на языке Python для работы с реляционными СУБД с применением технологии ORM.
* Alembic — библиотека для миграции к базе данных. Поддерживает возможность создания автоматических миграций на основе SqlAlchemy. Этот брокер сообщений используется в крупных приложениях для асинхронного отказоустойчивого обмена данными. Для асинхронного Python не имеет альтернатив.
* Uvicorn — реализация веб-сервера ASGI для Python. До недавнего времени в Python отсутствовал минимальный низкоуровневый интерфейс сервера / приложения для асинхронных фреймворков. Спецификация ASGI восполняет этот пробел и означает, что теперь мы можем приступить к созданию общего набора инструментов, который можно использовать во всех async-фреймворках.
* Pydantic — это библиотека Python, созданная Сэмюэлем Колвином, которая упрощает процесс проверки данных. Это универсальный инструмент, который можно использовать в различных сферах, таких как создание API, работа с базами данных и обработка данных в проектах. Библиотека имеет простой и интуитивно понятный синтаксис, позволяющий легко определять и проверять модели данных.
* FastAPI Users — самая популярная и многофункциональная библиотека для управления пользователями.
* aiogoogle — асинхронная библиотека для работы с Google API

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:usdocs/QRkot.git
cd QRkot
```

Создать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```

Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
alembic upgrade head
```

Запустить проект:
```bash
uvicorn app.main:app
```

#### Полный список запросов API находятся в документации

Ознакомиться с полным функционалом и примерами можно по эндпоинту http://127.0.0.1:8000/redoc


Автор: [Балакин Андрей](https://github.com/usdocs)

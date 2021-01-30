> Сайт находится в разработке.
> 
> Это сайт делается в целях изучения Django.

# Интернет магазин на Django + Python.

Готовый вариант можно посмотреть по ссылке: [derevo116.ru](http://derevo116.ru)

## Используемые технологии:

### BackEnd:

- Python 3.8
- Django 3.1

БД:

- локальная: Sqlite3
- на сервере: Postgresql

Дополнительные модули:

1.  django_summernote

настройки для wysiwig редактора в админке

2.  fieldsets\_with\_inlines

[https://pypi.org/project/django-fieldsets-with-inlines/](https://pypi.org/project/django-fieldsets-with-inlines/)

Расширяет функционал admin.ModelAdmin

3.  sorl.thumbnail

[https://github.com/jazzband/sorl-thumbnail](https://github.com/jazzband/sorl-thumbnail)

Делает превью картинок в шаблоне.

### FronEnd:

Верстка выполнена с помощью **Bootstrap CSS v5.0.0-alpha2.**

Корзина сделана на чистом **JavaScript**.

Основной принцип работы JS:

1.  отправка POST запросов с данными о заказе и товарах на сервер.
2.  Сервер полученные данные обрабатывает и записывает в сессию.
3.  Далее данные подставляются из сессии в шаблон.

* * *

С удовольствием принимаются замечания, советы, рекомендацию по улучшению кода и сайта.

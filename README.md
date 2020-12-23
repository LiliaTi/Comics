# Публикация комиксов

Данный проект позволяет автоматически публиковать в Вашей группе         [вконтакте](https://vk.com/feed) случайный комикс c сайта [xkcd.com](https://xkcd.com/)

## Как установить

Создайте в корне проекта файл `.env` и заполните Ваши данные: client_id, access_token, group_id

```python
VK_CLIENT_ID=YOUR_CLIENT_ID
VK_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
VK_GROUP_ID=YOUR_GROUP_ID
```
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```
## Как запустить 

Введите в консоль следущую команду:

```python
python main.py
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org.](https://dvmn.org/modules/)

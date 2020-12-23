import requests
import random


def get_image_info(url):
    response = requests.get(url)
    response.raise_for_status()
    image_info = response.json()
    title = image_info['safe_title']
    return {
        'image_url': image_info['img'],
        'comment': image_info['alt'],
        'image_name': f'{title}.png',
        'num': image_info['num']
    }


def load_image(image_info):
    response = requests.get(image_info['image_url'], verify=False)
    response.raise_for_status()
    with open(image_info['image_name'], 'wb') as file:
        file.write(response.content)


def get_url_of_random_comic():
    url_of_current_comic = 'http://xkcd.com/info.0.json'
    image_info = get_image_info(url_of_current_comic)
    num = image_info['num']
    random_comic = random.randint(1, num)
    return f'http://xkcd.com/{random_comic}/info.0.json'


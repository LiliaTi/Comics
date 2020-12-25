import requests


def catch_vk_error(response_json_content):
    return 'error' in response_json_content


def get_upload_url(access_token, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'group_id': group_id,
        'access_token': access_token,
        'v': '5.126'
    }
    response = requests.get(url, params=params)
    json_content = response.json()
    if catch_vk_error(json_content):
        return None
    else:
        return json_content['response']['upload_url']


def upload_photo_to_server(image_name, upload_url):
    with open(image_name, 'rb') as file:
        files = {
            'photo': file
        }
        response = requests.post(upload_url, files=files)
    json_content = response.json()
    if catch_vk_error(json_content):
        return None
    else:
        return json_content


def save_wall_photo(access_token, group_id,
                    upload_photo_to_server_result):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'group_id': group_id,
        'photo': upload_photo_to_server_result['photo'],
        'server': upload_photo_to_server_result['server'],
        'hash': upload_photo_to_server_result['hash'],
        'access_token': access_token,
        'v': '5.126'
    }
    response = requests.post(url, params)
    json_content = response.json()
    if catch_vk_error(json_content):
        return None
    else:
        return json_content


def post_to_wall(access_token, group_id, save_wall_photo_result, message):
    url = 'https://api.vk.com/method/wall.post'
    owner_id = save_wall_photo_result['response'][0]['owner_id']
    media_id = save_wall_photo_result['response'][0]['id']
    params = {
        'owner_id': f'-{group_id}',
        'from_group': 1,
        'attachments': f'photo{owner_id}_{media_id}',
        'message': message,
        'access_token': access_token,
        'v': '5.126'
    }
    response = requests.post(url, params)
    json_content = response.json()
    if catch_vk_error(json_content):
        return None
    else:
        return json_content


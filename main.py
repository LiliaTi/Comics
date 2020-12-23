import os
from dotenv import load_dotenv
from pprint import pprint
import comic_functions
import vk_functions


def main():
    load_dotenv()
    access_token = os.getenv('VK_ACCESS_TOKEN')
    group_id = os.getenv('VK_GROUP_ID')

    url_of_comic = comic_functions.get_url_of_random_comic()
    image_info = comic_functions.get_image_info(url_of_comic)
    comic_functions.load_image(image_info)

    image_name = image_info['image_name']

    upload_url = vk_functions.get_upload_url(access_token, group_id)
    upload_photo_to_server_result = vk_functions.upload_photo_to_server(
        image_name,
        upload_url)
    save_wall_photo_result = vk_functions.save_wall_photo(access_token,
                                                          group_id,
                                                          upload_photo_to_server_result)
    response = vk_functions.post_to_wall(access_token,
                                         group_id,
                                         save_wall_photo_result,
                                         image_info['comment'])
    pprint(response)
    os.remove(image_name)


if __name__ == '__main__':
    main()

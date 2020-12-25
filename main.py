import os
from dotenv import load_dotenv
import comic_functions
import vk_functions


def main():
    load_dotenv()
    access_token = os.getenv('VK_ACCESS_TOKEN')
    group_id = os.getenv('VK_GROUP_ID')

    comic_url = comic_functions.get_random_comic_url()
    image_info = comic_functions.get_image_info(comic_url)
    comic_functions.load_image(image_info)

    image_name = image_info['image_name']
    try:
        upload_url = vk_functions.get_upload_url(access_token, group_id)
        server_result = vk_functions.upload_photo_to_server(
            image_name,
            upload_url)
        saved_photo = vk_functions.save_wall_photo(access_token,
                                                   group_id,
                                                   server_result)
        vk_functions.post_to_wall(access_token,
                                  group_id,
                                  saved_photo,
                                  image_info['comment'])
    finally:
        os.remove(image_name)


if __name__ == '__main__':
    main()

import vk_api


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.photos.get(album_id=album_id, group_id=group_id)['items']
    for im in response:
        print(f"url: {im['sizes'][-1]['url']}, size:{im['sizes'][-1]['width']}x{im['sizes'][-1]['height']}")


if __name__ == '__main__':
    main()
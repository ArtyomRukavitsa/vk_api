import vk_api
import datetime


def main():
    login, password = LOGIN, PASSWORD  # Логин и пароль пользователя
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5)
    if response['items']:
        for i in response['items']:
            value = datetime.datetime.fromtimestamp(i['date'])
            print(value.strftime('%Y-%m-%d'), value.strftime('%H:%M:%S'))
            print(i['text'])


if __name__ == '__main__':
    main()
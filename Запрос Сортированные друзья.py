import vk_api
import json


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.friends.get(fields="bdate, city")['items']
    resp = sorted(response, key=lambda x: x['last_name'])
    for i in resp:
        try:
            print(i['first_name'], i['last_name'], i['bdate'] )
        except KeyError as e:
            print(i['first_name'], i['last_name'])


if __name__ == '__main__':
    main()
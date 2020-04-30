import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def get_id():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.photos.get(album_id=album_id, group_id=group_id)['items']
    photo = response[random.randint(0, len(response) - 1)]
    return f"photo{photo['owner_id']}_{photo['id']}"


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, id_сообщества)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Отправляю случайную фотографию из основного альбома :))",
                             random_id=random.randint(0, 2 ** 64),
                             attachment=get_id())


if __name__ == '__main__':
    main()
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime
import requests
import sys

DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


def main():
    vk_session = vk_api.VkApi(
        token=token)
    # токен к моему сообществу
    longpoll = VkBotLongPoll(vk_session, id)  # id сообщества
    need_city = True
    city = None
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            if need_city:
                city = event.obj.message['text']
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Отлично, выбери тип карты",
                                 random_id=random.randint(0, 2 ** 64),
                                 keyboard=open('keyboard.json', "r", encoding="UTF-8").read())
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Отправляю случайную фотографию из основного альбома :))",
                                 random_id=random.randint(0, 2 ** 64),
                                 keyboard={"buttons":[],"one_time":"true"})
                need_city = not need_city


if __name__ == '__main__':
    main()
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime

DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)
    # токен к моему сообществу
    longpoll = VkBotLongPoll(vk_session, id)  # id сообщества
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            try:
                answer = event.obj.message['text'].split('-')
                year, month, day = answer[0], answer[1], answer[2]
                weekday = DAYS[datetime.datetime(int(year), int(month), int(day)).weekday()]
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"День недели для даты {event.obj.message['text']}: {weekday}",
                                 random_id=random.randint(0, 2 ** 64))
            except ValueError:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Мне кажется, что ты ввел неверное значение месяца или дня.\nДавай еще раз!",
                                 random_id=random.randint(0, 2 ** 64))
            except IndexError:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Введи дату в формате YYYY-MM-DD",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
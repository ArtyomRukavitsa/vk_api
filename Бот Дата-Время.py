import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime
import pytz

DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)
    # токен к моему сообществу
    longpoll = VkBotLongPoll(vk_session, id)  # id сообщества
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if 'время' in event.obj.message['text'] or \
                    'число' in event.obj.message['text'] or \
                    'дата' in event.obj.message['text'] or \
                    'день' in event.obj.message['text']:
                date_and_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
                date, time = str(date_and_time).split()[0], str(date_and_time).split()[1].split('.')[0]
                weekday = DAYS[date_and_time.today().weekday()]
                vk = vk_session.get_api()
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Сегодняшняя дата: {date}\nТекущее время (UTC+3): {time}\nДень недели: {weekday}",
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk = vk_session.get_api()
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"А я умею говорить, какой сегодня день недели и не только!\n"
                                 f"Твое сообщение должно содежать слово 'время', или 'дата', или 'день', или 'число'",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
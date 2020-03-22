import wikipedia
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


wikipedia.set_lang('ru')


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)
    # токен к моему сообществу
    longpoll = VkBotLongPoll(vk_session, id)  # id сообщества
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            try:
                answer = wikipedia.summary(f"{event.obj.message['text']}", sentences=5)
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"{answer}",
                                 random_id=random.randint(0, 2 ** 64))
            except wikipedia.exceptions.DisambiguationError:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Много статьей могут относитсься к твоему сообщению. Напиши точнее.",
                                 random_id=random.randint(0, 2 ** 64))
            except wikipedia.exceptions.PageError:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Увы, но на Википедии такой статьи нет. Попробуй еще раз!",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()